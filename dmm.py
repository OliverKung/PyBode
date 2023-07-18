# Digitam Multimeter Driver for VXI instrument. Basically write for DMM6500/7510 Series. and 3446X Serise
import vxi11
from enum import Enum

class signal_type(Enum):
    DC = 0
    AC = 1
    dc = 0
    ac = 1

class resistance_method(Enum):
    two_wire=0
    four_wire=1

class DMM:

    def __init__(self,addr,model):
        self.addr=addr
        self.model=model
        self.instr=vxi11.Instrument(self.addr)
        self.instr.write("SYST:BEEP")
        print(self.instr.ask("*IDN?"))

    def voltage(self,mode:signal_type = signal_type.dc):
        if(mode==signal_type.dc):
            return float(self.instr.ask(":MEAS:VOLT:DC?"))
        if(mode==signal_type.ac):
            return float(self.instr.ask(":MEAS:VOLT:AC?"))

    def current(self,mode:signal_type = signal_type.dc):
        if(mode==signal_type.dc):
            return float(self.instr.ask(":MEAS:CURR:DC?"))
        if(mode==signal_type.ac):
            return float(self.instr.ask(":MEAS:CURR:AC?"))

    def resistance(self,mode:resistance_method=resistance_method.two_wire):
        if(mode==resistance_method.two_wire):
            return float(self.instr.ask(":MEAS:RES?"))
        if(mode==resistance_method.four_wire):
            return float(self.instr.ask(":MEAS:FRES?"))

if __name__=="__main__":
    my_dmm=DMM("192.168.2.128","34465A")

    # print(type(my_dmm.voltage(signal_type.ac)))
    # print(my_dmm.current(signal_type.dc))
    # print(my_dmm.resistance(resistance_method.two_wire))