# MSO5000 Series Oscilloscope python vxi11 lib.
import vxi11
import serial
import yaml
from enum import Enum
import os
import time
from UIP_TypeDef import interface_Enum
import instru_socket

class channel_number(Enum):
    channel1="channel1"
    channel2="channel2"
    channel3="channel3"
    channel4="channel4"

class UIP_OSC:
    def __init__(self,addr,model,interface:interface_Enum,\
                 port=5555,\
                 baudrate=9600,\
                ):
        self.addr=addr
        self.model=model
        ## create communication interface of instrument
        match interface:
            case(interface_Enum.serial):
                try:
                    self.serialinterface = serial.Serial(self.addr,baudrate=baudrate,timeout=5)
                    self.instr = self.serialinterface
                except:
                    print("Failed to Create Serial Bus at "+self.addr)
            case(interface_Enum.socket):
                try:
                    self.socketinterface = instru_socket.instru_socket()
                    self.socketinterface.connect((self.addr,port))
                    self.instr = self.socketinterface
                except:
                    print("Failed to Create Socket Bus at "+self.addr)
            case(interface_Enum.LXI):
                try:
                    self.LXIinterface = vxi11.Instrument(self.addr)
                    self.instr = self.LXIinterface
                except:
                    print("Failed to Create LXI Bus at "+self.addr)
        ## beep of OSC to confirm connected
        self.instr.write("SYST:BEEP ON")
        print(self.instr.ask("*IDN?"))
        self.instr.write("SYST:BEEP OFF")
    
    def load_setting_yaml(self):
        try:
            with open("./instruDriver/OSC_YAML/"+self.model+".yaml","r") as f:
                self.commandDict = yaml.load(f,Loader=yaml.FullLoader)
        except:
            print("Failed to Read YAML File!")
    
    def autoscale(self):
        self.instr.write(self.commandDict["autosetCommand"]["autoset"])
        time.sleep(1)
    
    def vrms(self,channel:channel_number):
        cmd:str = self.commandDict["measureCommand"]["command"]+\
            self.commandDict["measureCommand"]["item"]["command"]+\
            self.commandDict["measureCommand"]["item"]["endfix_single"]
        cmd.replace("<src>",self.commandDict["measureCommand"]["item"]["src"][channel.value])
        cmd.replace("<item>",self.commandDict["measureCommand"]["item"]["vrms"])
        return float(self.instr.ask(cmd))

    def freq(self,channel):
        cmd = ":MEAS:ITEM? FREQ,"+channel.value
        return float(self.instr.ask(cmd))

    def phase(self,channelA,channelB):
        cmd = ":MEAS:ITEM? RRPH,"+channelA.value+","+channelB.value
        return float(self.instr.ask(cmd))

    def setAcquire(self,memdepth:memory_store_depth=memory_store_depth.depth_AUTO,\
        samplemode:sample_method=sample_method.normal):
        self.instr.write(":ACQ:TYPE "+samplemode.value)
        self.instr.write(":ACQ:MDEP "+memdepth.value)
        # print("Memory Depth of "+self.model+" locates at "+self.addr+" set to "+self.instr.ask(":ACQ:MDEP?"))
        # print("Acquire Mode of "+self.model+" locates at "+self.addr+" set to "+self.instr.ask(":ACQ:TYPE?"))
        time.sleep(1)

    def getScreenshoot(self,file_name:str):
        with open(file_name,"wb") as image:
            self.instr.write(":DISPlay:DATA?")
            img=self.instr.read_raw()
            image.write(img[11:])# remove head 11 meaning less bytes
            image.close()

    def setTimebaseScale(self,timebase_scale):
        self.instr.write(":TIM:SCAL "+str(timebase_scale))
    
    def setChannelOffet(self,channel,offset):
        self.instr.write(":"+channel.value+":OFFS "+str(offset))

    def getChannelScale(self,channel):
        return float(self.instr.ask(":"+channel.value+":SCAL?"))
    
    def setChannelScale(self,channel,scale):
        self.instr.write(":"+channel.value+":SCAL "+str(scale))
    
    def getTimebaseScale(self):
        return float(self.instr.ask(":TIM:SCAL?"))
    
    def setChannelCouple(self,channel,couple:couple_type):
        self.instr.write(":"+channel.value+":COUP "+couple.value)
    
    def setTriggerChannel(self,channel):
        self.instr.write(":TRIG:EDGE:SOUR "+channel.value)
    
    def setTriggerLevel(self,voltage):
        self.instr.write(":TRIG:EDGE:LEV "+str(voltage))

    def setAverageTimes(self,averagetimes):
        self.instr.write(":ACQ:AVER "+str(2**averagetimes))
    
    def setChannelAtte(self,channel,atte):
        self.instr.write(":"+channel.value+":PROB "+atte)
    
    def setChannelUnit(self,channel,unit:str):
        self.instr.write(":"+channel.value+":UNIT "+unit)
    
    def getChannelAtte(self,channel):
        Atte=self.instr.ask(":"+channel.value+":PROB?")
        return float(Atte)
    
if __name__=="__main__":
    my_osc=mso5k("192.168.31.32","MSO5072")
    print(my_osc.voltage(channel_number.ch1,wave_parameter.rms))
    print(my_osc.freq(channel_number.ch1))
    my_osc.setAcquire(samplemode=sample_method.normal,memdepth=memory_store_depth.depth_1M)
    # my_osc.autoscale()
    # time.sleep(10)
    print(time.time())
    my_osc.saveChanneltoFile("/home/inststa/inststa/data/channel2.csv",channel_number.ch1,data_mode=memory_store_method.RAW_data,memory_length=1000000)
    my_osc.getScreenshoot("/home/inststa/inststa/image/sc1.bmp")
    print(time.time())
    os.system("cp -r /home/inststa/inststa/data/ /home/inststa/ERP/data")
    