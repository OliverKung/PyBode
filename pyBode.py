from MSO5K import *
from SDG2000X import *
import numpy as np
import pandas as pd
import math
from tqdm import tqdm
import plotly.io as pio
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import argparse

def show_in_window(fig):
    import sys, os
    import plotly.offline
    from PyQt5.QtCore import QUrl
    from PyQt5.QtWebEngineWidgets import QWebEngineView
    from PyQt5.QtWidgets import QApplication
    
    plotly.offline.plot(fig, filename='./name.html', auto_open=False)
    
    app = QApplication(sys.argv)
    web = QWebEngineView()
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "name.html"))
    print(file_path)
    web.load(QUrl.fromLocalFile(file_path))
    web.show()
    sys.exit(app.exec_())


class PyBode():
    def __init__(self,osc_addr,afg_addr):
        self.osc_addr=osc_addr
        self.afg_addr=afg_addr
        self.osc=mso5k(osc_addr,"MSO5072")
        self.afg=SDG2000X(afg_addr,"SDG2042X")
        self.syncTriggerEnable = False
    
    def run(self,startFreq,stopFreq,totalPoints,Ampilitude,\
            ExcitationChannel:channel_number,\
            inputChannel:channel_number,\
            outputChannel:channel_number,\
            syncTrigger:channel_number,\
            ):
        my_osc=self.osc
        my_dsg=self.afg

        freq_list=np.logspace(math.log(startFreq,10),math.log(stopFreq,10),int(totalPoints),endpoint = True)
        df=pd.DataFrame({}, columns=['freq', 'gain', 'phase'])

        timebase_scale=10
        my_osc.setTimebaseScale(10)

        channel1_scale=my_osc.getChannelScale(inputChannel)
        channel2_scale=my_osc.getChannelScale(outputChannel)

        with open('.\\ExampleData\\bode_data_'+time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))+".csv","w") as f:
            for freq in tqdm(freq_list):
                my_dsg.set_freq_amp(freq,Ampilitude,ExcitationChannel)

                if(self.syncTriggerEnable == True):
                    my_dsg.set_freq_amp(freq,1,syncTrigger)    #set signal source

                my_osc.setTimebaseScale(0.25*1/freq)
                time.sleep(0.01 if 0.01>4*1/freq else 4*1/freq) #wait for measure
                
                voltage1=my_osc.voltage(inputChannel,wave_parameter.Peak2Peak)
                voltage2=my_osc.voltage(outputChannel,wave_parameter.Peak2Peak)

                while(voltage1>channel1_scale*8):#When amplitude is too large, auto scale
                    print("CH1 voltage scale too large, voltage is "+str(voltage1)+",scale is "+str(voltage1))
                    my_osc.setChannelScale(inputChannel,channel1_scale*8)
                    time.sleep(0.01 if 0.01>4*1/freq else 4*1/freq)
                    channel1_scale=channel1_scale*8
                    voltage1=my_osc.voltage(inputChannel,wave_parameter.Peak2Peak)
                
                while(voltage2>channel2_scale*8):#When amplitude is too large, auto scale
                    print("CH2 voltage scale too large, voltage is "+str(voltage2)+",scale is "+str(voltage2))
                    my_osc.setChannelScale(outputChannel,channel2_scale*8)
                    time.sleep(0.01 if 0.01>4*1/freq else 4*1/freq)
                    channel2_scale=channel2_scale*8
                    voltage2=my_osc.voltage(outputChannel,wave_parameter.Peak2Peak)

                if(voltage1<2*channel1_scale or voltage1>6*channel1_scale):
                    my_osc.setChannelScale(inputChannel,voltage1/4)#AutoScale when signal is too small
                    channel1_scale = voltage1/4
                if(voltage2<2*channel2_scale or voltage2>6*channel2_scale):
                    my_osc.setChannelScale(outputChannel,voltage2/4)
                    channel2_scale = voltage2/4

                time.sleep(0.01 if 0.01>4*1/freq else 4*1/freq) #wait for measure

                voltage1=my_osc.voltage(inputChannel,wave_parameter.RMS)
                voltage2=my_osc.voltage(outputChannel,wave_parameter.RMS)
                phase=my_osc.phase(inputChannel,outputChannel)
                gain=20*math.log(voltage2/voltage1,10)

                f.write(str(freq)+","+str(voltage1)+","+str(voltage2)+","+str(gain)+","+str(phase)+"\r")
                df.loc[len(df.index)]=[freq,gain,phase]
            f.close()
        fig = make_subplots(rows = 2, cols = 1)
        fig.add_trace(go.Scatter(x=df['freq'], y=df['gain'], mode='lines', name='Gain'), row = 1, col = 1)
        fig.add_trace(go.Scatter(x=df['freq'], y=df['phase'], mode='lines', name='Phase'), row = 2, col = 1)
        fig.update_xaxes(type="log", exponentformat="power")
        fig.update_layout()
        show_in_window(fig)
    def setChannel(self,excitionchannel,inputchannel,outputchannel,\
                   synctrigger,syncchannel,samplemethod,averageTimes):
        if(self.syncTriggerEnable == True):
            self.osc.setChannelCouple(inputchannel,couple_type.ac)
            self.osc.setChannelCouple(outputchannel,couple_type.ac)
            self.osc.setChannelCouple(syncchannel,couple_type.ac)
            self.osc.setChannelOffet(inputchannel,0)
            self.osc.setChannelOffet(outputchannel,0)
            self.osc.setChannelOffet(syncchannel,0)
            self.osc.setAcquire(samplemode=samplemethod)
            self.osc.setAverageTimes(averageTimes)
            self.osc.setTriggerChannel(syncchannel)
            self.osc.setTriggerLevel(0)

            self.afg.set_waveform_type(excitionchannel,waveform_type.sin)
            self.afg.set_waveform_type(synctrigger,waveform_type.square)
            self.afg.setChannelOutputState(excitionchannel,1)
            return;
        else:
            self.osc.setChannelCouple(inputchannel,couple_type.ac)
            self.osc.setChannelCouple(outputchannel,couple_type.ac)
            self.osc.setChannelOffet(inputchannel,0)
            self.osc.setChannelOffet(outputchannel,0)
            self.osc.setAcquire(samplemode=samplemethod)

            self.osc.setTriggerChannel(inputchannel)
            self.osc.setTriggerLevel(0)

            self.afg.set_waveform_type(excitionchannel,waveform_type.sin)
            self.afg.setChannelOutputState(excitionchannel,1)
            return;

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s","--sample-method", type=str,default="normal",help="Sample Method: Normal,Peak,Average and Hi-Res")
    parser.add_argument("-aT","--average-times",type=int,default=4,help="the average times of average sample, input the power of average times, for example, default value is 4, this means 2^4=16 times average")
    parser.add_argument("-sF","--startFreq",type=float,default=1e3,help="Sweep start frequency in Hz")
    parser.add_argument("-eF","--endFreq",type=float,default=1e6,help="Sweep stop frequency in Hz")
    parser.add_argument("-p","--points",type=int,default=100,help="total sweep points")
    parser.add_argument("-a","--amplitude",type=float,default=0.1,help="excition signal amplitude")
    parser.add_argument("-eC","--excition-channel",type=str, default="ch1",help="the excition channel of function generator,default is \"ch1\"")
    parser.add_argument("-iC","--input-channel",type=str,default="ch1",help="network input channel of osc,default is \"ch1\"")
    parser.add_argument("-oC","--output-channel",type=str,default="ch2",help="network output channel of osc,default is \"ch2\"")
    parser.add_argument("-sT","--sync-trigger",type=str,default="ch2",help="the sync trigger function generator sync number, default is \*ch2\*")
    parser.add_argument("-sC","--sync-channel",type=str,default="ch3",help="the sync trigger channel number, default is \*ch2\*")
    parser.add_argument("-sTE","--sync-trigger-enable",type=str,default="false",help="sync Trigger function enable, default is flase")
    parser.add_argument("--afg-ip",type=str,default="",help="IP addr of arbitary function generator")
    parser.add_argument("--osc-ip",type=str,default="",help="IP addr of oscilliscope")
    return parser.parse_args()

if __name__=="__main__":
    args = parse_args()
    print(args)
    #arguments correction check
    if(args.afg_ip == ""):
        print("\033[0;31;40mERROR! YOU MUST SET IP ADDR OF AFG\033[0m")
    if(args.osc_ip == ""):
        print("\033[0;31;40mERROR! YOU MUST SET IP ADDR OF OSC\033[0m")
    uPyBode=PyBode(args.osc_ip,args.afg_ip)

    if(args.sync_trigger_enable == "true"):
        uPyBode.syncTriggerEnable = True

    excitionChannel=channel_number.ch1
    inputChannel=channel_number.ch1
    outputChannel=channel_number.ch2
    syncTrigger=channel_number.ch2
    syncChannel=channel_number.ch3
    sampleMethod = sample_method.normal
    for method in sample_method:
        if(args.sample_method == method.name):
            sampleMethod=method
    print(sampleMethod)
    for channel in channel_number:
        if(args.excition_channel == channel.name):
            excitionChannel=channel
        if(args.input_channel == channel.name):
            inputChannel=channel
        if(args.output_channel == channel.name):
            outputChannel=channel
        if(args.sync_trigger == channel.name):
            syncTrigger=channel
        if(args.sync_channel == channel.name):
            syncChannel=channel
    uPyBode.setChannel(excitionChannel,inputChannel,outputChannel,\
                       syncTrigger,syncChannel,sampleMethod,args.average_times)

    uPyBode.run(args.startFreq,args.endFreq,args.points,args.amplitude\
                ,ExcitationChannel=excitionChannel,inputChannel=inputChannel,outputChannel=outputChannel,\
                syncTrigger=syncTrigger)
