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
        time.sleep(1)
        self.instru_socket.write("")
        IDN_str+=self.instru_socket.recv(100).decode()
        print(IDN_str)
        # somehow, if there is no time.sleep, the IDN string will be cut off. Maybe some bug of socat
        self.instru_socket.write("SYST:REM")

    def channel_on(self,channel:supply_channel_number=supply_channel_number.all):
        if(channel != supply_channel_number.all):
            cmd="INST:SEL "+channel.value
            self.instru_socket.write(cmd)
            self.instru_socket.write("SOUR:CHAN:OUTPUT ON")
        else:
            self.instru_socket.write("OUTP:STAT ON")

    def channel_off(self,channel:supply_channel_number=supply_channel_number.all):
        if(channel != supply_channel_number.all):
            cmd="INST:SEL "+channel.value
            self.instru_socket.write(cmd)
            self.instru_socket.write("SOUR:CHAN:OUTPUT OFF")
        else:
            self.instru_socket.write("OUTP:STAT OFF")

    def set_voltage(self,channel:supply_channel_number,voltage:float):
        if(channel!=supply_channel_number.all):
            cmd="INST:SEL "+channel.value
            self.instru_socket.write(cmd)
            cmd="SOUR:VOLT "+str(voltage)
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
    my_supply=IT63XX_socket("127.0.0.1",65501)
    my_supply.channel_off()
    # my_supply.channel_on()
    # time.sleep(1)
    # my_supply.set_voltage(supply_channel_number.ch1,54.321)
    # my_supply.set_voltage(supply_channel_number.ch2,12.345)
    # my_supply.set_voltage(supply_channel_number.ch3,4.99)
    # print(my_supply.meas_voltage(supply_channel_number.ch1))
    # my_supply.channel_on()
    # # my_supply.channel_off()
    # time.sleep(2)
    # print(my_supply.meas_current(supply_channel_number.ch1))