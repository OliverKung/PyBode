# MSO5000 Series Oscilloscope python vxi11 lib.
import vxi11
import serial
import socket
from enum import Enum
import os
import time
from UIP_TypeDef import interface_Enum
import instru_socket

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
                except:
                    print("Failed to Create Serial Bus at "+self.addr)
            case(interface_Enum.socket):
                try:
                    self.socketinterface = instru_socket.instru_socket()
                    self.socketinterface.connect((self.addr,port))
                except:
                    print("Failed to Create Socket Bus at "+self.addr)
            case(interface_Enum.LXI):
                try:
                    self.LXIinterface = vxi11.Instrument(self.addr)
                except:
                    print("Failed to Create LXI Bus at "+self.addr)
        self.instr = 
        self.instr.write("SYST:BEEP ON")
        print(self.instr.ask("*IDN?"))
        self.instr.write("SYST:BEEP OFF")
    
    def autoscale(self):
        self.instr.write(":AUT")
        time.sleep(1)
    
    def voltage(self,channel:channel_number,items:wave_parameter):
        self.instr=vxi11.Instrument(self.addr)
        cmd = ":MEAS:ITEM? "+items.value+","+channel.value
        return float(self.instr.ask(cmd))

    def freq(self,channel:channel_number):
        self.instr=vxi11.Instrument(self.addr)
        cmd = ":MEAS:ITEM? FREQ,"+channel.value
        return float(self.instr.ask(cmd))

    def phase(self,channelA:channel_number,channelB:channel_number):
        self.instr=vxi11.Instrument(self.addr)
        cmd = ":MEAS:ITEM? RRPH,"+channelA.value+","+channelB.value
        return float(self.instr.ask(cmd))

    def saveChanneltoFile(self,\
        file_name:str,channel:channel_number,\
        data_mode:memory_store_method=memory_store_method.screen_only,\
        memory_length:int=1000):
        with open(file_name,"w") as f:
            print("Store "+str(channel)+" "+str(memory_length)+" points data to "+file_name)
            if(data_mode==memory_store_method.screen_only):
                self.instr.write(":WAV:MODE NORM")
                self.instr.write(":WAV:POIN "+str(memory_length))
                self.instr.write(":WAV:FORMAT ASCII")
                data_line=self.instr.ask(":WAV:DATA?")
                data_point=data_line.split(",")
                f.write("Voltage\r\n")
                data_point[0]=data_point[0][11:]
                for data in data_point:
                    f.write(data+"\r\n")
            if(data_mode==memory_store_method.RAW_data):
                self.instr.write(":WAV:MODE RAW")
                self.instr.write(":WAV:POIN "+str(memory_length))
                self.instr.write(":WAV:FORMAT ASCII")
                self.instr.write(":STOP")
                print("start time:")
                print(time.time())
                data_line=self.instr.ask(":WAV:DATA?")
                print(time.time())
                print(data_line)
                data_point=data_line.split(",")
                f.write("Voltage\r\n")
                data_point[0]=data_point[0][11:]# remove head meaning less bytes
                for data in data_point:
                    f.write(data+"\r\n")
                self.instr.write(":RUN")
            print(channel.value+" Data of "+self.model+" locates at "+self.addr+" saved to "+file_name)

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
    
    def setChannelOffet(self,channel:channel_number,offset):
        self.instr.write(":"+channel.value+":OFFS "+str(offset))

    def getChannelScale(self,channel:channel_number):
        return float(self.instr.ask(":"+channel.value+":SCAL?"))
    
    def setChannelScale(self,channel:channel_number,scale):
        self.instr.write(":"+channel.value+":SCAL "+str(scale))
    
    def getTimebaseScale(self):
        return float(self.instr.ask(":TIM:SCAL?"))
    
    def setChannelCouple(self,channel:channel_number,couple:couple_type):
        self.instr.write(":"+channel.value+":COUP "+couple.value)
    
    def setTriggerChannel(self,channel:channel_number):
        self.instr.write(":TRIG:EDGE:SOUR "+channel.value)
    
    def setTriggerLevel(self,voltage):
        self.instr.write(":TRIG:EDGE:LEV "+str(voltage))

    def setAverageTimes(self,averagetimes):
        self.instr.write(":ACQ:AVER "+str(2**averagetimes))
    
    def setChannelAtte(self,channel:channel_number,atte):
        self.instr.write(":"+channel.value+":PROB "+atte)
    
    def setChannelUnit(self,channel:channel_number,unit:str):
        self.instr.write(":"+channel.value+":UNIT "+unit)
    
    def getChannelAtte(self,channel:channel_number):
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
    