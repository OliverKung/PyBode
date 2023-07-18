import serial
from enum import Enum 
import time

class resistance_method(Enum):
    two_wire=0
    four_wire=1

class K2015:

    def __init__(self,addr,mode="K2015"):
        self.ser=serial.Serial(addr,9600,timeout=5)
        self.ser.setDTR(False)
        self.ser.setRTS(False)
        print(self.serialASK("*IDN?"))

    def beep(self):
        self.ser.write("SYST:BEEP".encode("utf-8"))

    def resistance(self,mode:resistance_method=resistance_method.two_wire):
        if(mode==resistance_method.two_wire):
            return float(self.serialASK(":MEAS:RES?"))
        if(mode==resistance_method.four_wire):
            return float(self.serialASK(":MEAS:FRES?"))

    def setresistance(self,mode:resistance_method=resistance_method.two_wire):
        if(mode==resistance_method.two_wire):
            self.serialWrite(":CONF:RES")
        if(mode==resistance_method.four_wire):
            self.serialWrite(":CONF:FRES")
    
    def read(self):
        return float(self.serialASK(":READ?"))

    def serialWrite(self,cmd):
        self.ser.write((cmd+"\r").encode("utf-8"))

    def serialASK(self,cmd):
        self.ser.write((cmd+"\r").encode("utf-8"))
        return(self.ser.readline().decode().replace("\r\n",""))

# if __name__ == "__main__":
    # K2015X=K2015("COM9")
    # print(K2015X.setresistance(resistance_method.two_wire))
    # time.sleep(5)
    # print(K2015X.read())
    
