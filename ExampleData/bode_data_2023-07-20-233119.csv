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

class wavetype(Enum):
    sine = "sine"
    square = "square"
    ramp = "ramp"
    pulse = "pulse"
    noise = "noise"
    dc = "dc"

class sample_type(Enum):
    norm = "norm"
    peak = "peak"
    aver = "aver"
    hires = "hires"
class UIP_AFG:
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
        ## load YAML config file
        self.loadYAML()
        print("YAML version:"+self.commandDict["oscillscope"]["driverVersion"])
        ## beep of OSC to confirm connected
        self.instr.write("SYST:BEEP ON")
        print(self.instr.ask("*IDN?"))
        self.instr.write("SYST:BEEP OFF")
    
    def loadYAML(self):
        try:
            with open("./instruDriver/AFG_YAML/"+self.model+".yaml","r") as f:
                self.commandDict = yaml.load(f,Loader=yaml.FullLoader)
        except:
            print("Failed to Read YAML File!")

    def autoscale(self):# finish YAML version
        try:
            cmd = self.commandDict["autosetCommand"]["autoset"]
        except:
            print("autoset is supported by current version")
        self.instr.write(cmd)
        time.sleep(1)
    
    def measure(self,parameter:wave_parameter,channel1:channel_number,channel2:channel_number=channel_number.channel1):
        #finish YAML version
        try:
            cmd:str = self.commandDict["measureCommand"][parameter.value]
        except:
            print("measure " +parameter.value+" is not supported by current version YAML")
            return 0

        if(cmd.count("<src>") == 1):
            cmd=cmd.replace("<src>",self.commandDict["measureCommand"]["src"][channel1.value])
        else:
            cmd=cmd.replace("<src>",self.commandDict["measureCommand"]["src"][channel1.value],1)
            cmd=cmd.replace("<src>",self.commandDict["measureCommand"]["src"][channel2.value])
        return float(self.instr.ask(cmd))

    def acquireType(self,samplemode:sample_type):
        #finish YAML version
        try:
            cmd:str = self.commandDict["acquireCommand"]["command"]\
                      +self.commandDict["acquireCommand"]["type"]["command"]\
                      +self.commandDict["acquireCommand"]["type"][samplemode.value]
        except:
            print("acquire type setting is not supported by current version YAML")
            return 0
        return self.instr.write(cmd)

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
    
    def setChannelCouple(self,channel,couple):
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
    my_osc=UIP_OSC("192.168.32.112","DHO900",interface=interface_Enum.LXI)
    my_osc.autoscale()
    my_osc.acquireType(sample_type.hires)
    time.sleep(2)
    print(my_osc.measure(wave_parameter.freq,channel_number.channel1))
    print(my_osc.measure(wave_parameter.rise_rise_phase,channel_number.channel1,channel_number.channel3))

    