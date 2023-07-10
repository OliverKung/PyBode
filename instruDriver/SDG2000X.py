# MSO5000 Series Oscilloscope python vxi11 lib.
import vxi11
from enum import Enum
from typedef import channel_number,waveform_type

class SDG2000X:
    def __init__(self,addr,model):
        self.addr=addr
        self.model=model
        self.instr=vxi11.Instrument(self.addr)
        self.instr.write("SYST:BEEP ON")
        print(self.instr.ask("*IDN?"))
        self.instr.write("SYST:BEEP OFF")
    def set_sine_waveform(self,freq,amplitude,channel=1):
        if(channel == 1):
            channel_Str="C1"
        else:
            channel_Str="C2"
        self.instr.write(channel_Str+":BSWV AMP,"+str(amplitude))
        self.instr.write(channel_Str+":BSWV FRQ,"+str(freq))


if __name__=="__main__":
    my_dsg=SDG2000X("192.168.31.24","MSO5072")
    # print(my_dsg.instr.ask("C2:BSWV?"))
    # my_dsg.set_sine_waveform(1e8,1,2)
