import serial
from instru_socket import instru_socket
from enum import Enum
import time

class resistanceMethod(Enum):
    two_wire=0
    four_wire=1

class inputCouple(Enum):
    ac=0
    dc=1

class K2015_socket:

    def __init__(self,addr,port,mode="K2015"):
        self.instru_socket=instru_socket()
        self.instru_socket.connect((addr,port))
        self.instru_socket.settimeout(200)
        #self.ser.setDTresistanceMethodR(False)# not sure for socat controls ttyS,rts and dtr are disabled by default.
        #self.ser.setRTS(False)# not sure for socat controls ttyS,rts and dtr are disabled by default.
        self.instru_socket.write("*IDN?")
        IDN_str=self.instru_socket.recv(100).decode()
        print(IDN_str)
        time.sleep(1)

    def beep(self):
        self.instru_socket.write("SYST:BEEP")

    def resistance(self,mode:resistanceMethod=resistanceMethod.two_wire):
        if(mode==resistanceMethod.two_wire):
            return float(self.instru_socket.ask(":MEAS:RES?"))
        if(mode==resistanceMethod.four_wire):
            return float(self.instru_socket.ask(":MEAS:FRES?"))

    def setResistance(self,mode:resistanceMethod=resistanceMethod.two_wire):
        if(mode==resistanceMethod.two_wire):
            self.instru_socket.write(":CONF:RES")
        if(mode==resistanceMethod.four_wire):
            self.instru_socket.write(":CONF:FRES")
    
    def setVoltage(self,mode:inputCouple=inputCouple.dc):
        if(mode==inputCouple.dc):
            self.instru_socket.write(":CONF:VOLT:DC")
        if(mode==inputCouple.ac):
            self.instru_socket.write(":CONF:VOLT:AC")

    def setCurrent(self,mode:inputCouple=inputCouple.dc):
        if(mode==inputCouple.dc):
            self.instru_socket.write(":CONF:CURR:DC")
        if(mode==inputCouple.ac):
            self.instru_socket.write(":CONF:CURR:AC")
    
    def setFrequency(self):
        self.instru_socket.write(":CONF:FREQ")

    def setPeriod(self):
        self.instru_socket.write(":CONF:PER")
    
    def setTemparature(self):
        self.instru_socket.write(":CONF:TEMP")

    def read(self):
        return float(self.instru_socket.ask(":READ?"))

    def fetch(self):
        return float(self.instru_socket.ask(":FETCH?"))

if __name__ == "__main__":
    K2015X=K2015_socket("192.168.31.180",65502)
    # print(K2015X.setresistance(resistanceMethod.two_wire))
    # k=0
    # while k<100:
    #     print(K2015X.fetch())
    #     k=k+1
    #     time.sleep(1)
    
