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
    
    def run(self,startFreq,stopFreq,totalPoints,Ampilitude,\
            ExcitationChannel:channel_number,\
            inputChannel:channel_number,\
            outputChannel:channel_number):
        my_osc=self.osc
        my_dsg=self.afg

        freq_list=np.logspace(math.log(startFreq,10),math.log(stopFreq,10),int(totalPoints),endpoint = True)
        df=pd.DataFrame({}, columns=['freq', 'gain', 'phase'])

        my_osc.setChannelOffet(inputChannel,0)
        my_osc.setChannelOffet(outputChannel,0)

        my_dsg.setChannelOutputState(channel_number.ch2,1)
        my_dsg.setChannelOutputState(channel_number.ch1,1)
        timebase_scale=10
        my_osc.setTimebaseScale(10)

        channel1_scale=my_osc.getChannelScale(inputChannel)
        channel2_scale=my_osc.getChannelScale(outputChannel)

        with open('F:\SoftDev\Instruments\inststa\data\\bode_data_'+time.strftime("%Y-%m-%d-%H%M%S", time.localtime(time.time()))+".csv","w") as f:
            for freq in tqdm(freq_list):
                my_dsg.set_sine_waveform(freq,Ampilitude,ExcitationChannel)
                my_dsg.set_sine_waveform(freq,1,channel_number.ch1)    #set signal source
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
if __name__=="__main__":
    uPyBode=PyBode("192.168.31.32","192.168.31.24")
    uPyBode.run(1e3,10e6,100,0.05,channel_number.ch2,channel_number.ch1,channel_number.ch2)
