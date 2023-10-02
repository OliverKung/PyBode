# python Serial lib for IT63XX series power supply
# Now release in socket lib

import time
from instru_socket import *
from enum import Enum

class supply_channel_number(Enum):
    ch1="CH1"
    ch2="CH2"
    ch3="CH3"
    all="all"

class IT63XX_socket:
    def __init__(self,addr,port,model="IT6333A"):
        self.instru_socket=instru_socket()
        self.instru_socket.connect((addr,port))
        self.instru_socket.write("SYST:BEEP")
        self.instru_socket.write("*IDN?")
        IDN_str=self.instru_socket.recv(100).decode()
        print(IDN_str)
        # somehow, if there is no time.sleep, the IDN string will be cut off. Maybe some bug of socat
        # self.instru_socket.write("SYST:REM")

    def channel_on(self,channel:supply_channel_number=supply_channel_number.all):
        if(channel != supply_channel_number.all):
            cmd="INST:SEL "+channel.value
            self.instru_socket.write(cmd)
            self.instru_socket.write("OUTP ON")
        else:
            self.instru_socket.write("OUTP ON")

    def channel_off(self,channel:supply_channel_number=supply_channel_number.all):
        if(channel != supply_channel_number.all):
            cmd="INST:SEL "+channel.value
            self.instru_socket.write(cmd)
            self.instru_socket.write("OUTP OFF")
        else:
            self.instru_socket.write("OUTP OFF")

    def set_voltage(self,channel:supply_channel_number,voltage:float):
        if(channel!=supply_channel_number.all):
            cmd="INST:SEL "+channel.value
            self.instru_socket.write(cmd)
            cmd="VOLT "+str(voltage)
            self.instru_socket.write(cmd)

    def set_current(self,channel:supply_channel_number,current:float):
        if(channel!=supply_channel_number.all):
            cmd="INST:SEL "+channel.value
            self.instru_socket.write(cmd)
            cmd="SOUR:CURR "+str(current)
            self.instru_socket.write(cmd)

    def meas_voltage(self,channel:supply_channel_number):
        if(channel!=supply_channel_number.all):
            cmd="INST:SEL "+channel.value
            self.instru_socket.write(cmd)
            cmd="MEAS:VOLT?"
            self.instru_socket.write(cmd)
            return float(self.instru_socket.recv(1024).decode().replace("\n",""))

    def meas_current(self,channel:supply_channel_number):
        if(channel!=supply_channel_number.all):
            cmd="INST:SEL "+channel.value
            self.instru_socket.write(cmd)
            cmd="MEAS:CURR?"
            self.instru_socket.write(cmd)
            return float(self.instru_socket.recv(1024).decode().replace("\n",""))
            
    def beep(self):
        self.instru_socket.write("SYST:BEEP")

if __name__ == "__main__":
    my_supply=IT63XX_socket("192.168.32.162",5025)
    my_supply.set_voltage(supply_channel_number.ch1,0.1)
    my_supply.channel_on(supply_channel_number.ch1)
    time.sleep(0.5)
    # print("output on")
    for i in range(20):
        voltage = i*5/20
        print(voltage)
        my_supply.set_voltage(supply_channel_number.ch1,voltage)
        time.sleep(3)
    