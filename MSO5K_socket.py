# MSO5000 Series Oscilloscope python vxi11 lib.
# now released in socket lib
from instru_socket import instru_socket
from enum import Enum
from typedef import channel_number,wave_parameter

class memory_store_method(Enum):
    screen_only=0
    RAW_data=1


class mso5k_socket:
    def __init__(self,addr,port,model):
        self.addr=addr
        self.model=model
        self.instru_socket=instru_socket()
        self.instru_socket.connect((addr,port))
        self.instru_socket.settimeout(200)
        self.instru_socket.write("SYST:BEEP ON")
        print(self.instru_socket.ask("*IDN?"))
        self.instru_socket.write("SYST:BEEP OFF")
    
    def autoscale(self):
        self.instru_socket.write(":AUT")
    
    def voltage(self,channel:channel_number,items:wave_parameter):
        cmd = ":MEAS:ITEM? "+items.value+","+channel.value
        return float(self.instru_socket.ask(cmd))

    def freq(self,channel:channel_number):
        cmd = ":MEAS:ITEM? FREQ,"+channel.value
        return float(self.instru_socket.ask(cmd))

    def phase(self,channelA:channel_number,channelB:channel_number):
        cmd = ":MEAS:ITEM? RRPH,"+channelA.value+","+channelB.value
        return float(self.instru_socket.ask(cmd))

    def saveChanneltoFile(self,\
        file_name:str,channel:channel_number,\
        data_mode:memory_store_method=memory_store_method.screen_only,\
        memory_length:int=1000):
        with open(file_name,"w") as f:
            print("Store channel "+str(channel)+str(memory_length)+" points data to "+file_name)
        

if __name__=="__main__":
    my_osc=mso5k_socket("192.168.31.32",5555,"MSO5072")
    print(my_osc.voltage(channel_number.ch1,wave_parameter.rms))
    print(my_osc.freq(channel_number.ch1))
    my_osc.saveChanneltoFile("./channel1.csv",channel_number.ch1)
    # print(my_osc.phase(channel_number.ch1,channel_number.ch3))
    