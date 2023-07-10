import serial
from enum import Enum 
import time

class MeterCareLite:

    def __init__(self,addr,mode="MeterCareLite"):
        self.ser=serial.Serial(addr,115200,timeout=5)
        self.ser.setDTR(False)
        self.ser.setRTS(False)
        print("MeterCare Lite DS18B20 Temp")

    def serialASK(self):
        self.ser.write(("CARE_TEMP1?\r\n").encode("utf-8"))
        return(self.ser.readline().decode().replace("\r\n",""))

if __name__ == "__main__":
    MeterCareLiteX=MeterCareLite("COM3")
    print(MeterCareLiteX.serialASK())
    