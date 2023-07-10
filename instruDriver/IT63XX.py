# python Serial lib for IT63XX series power supply
import time
import serial
from enum import Enum

class supply_channel_number(Enum):
    ch1="CH1"
    ch2="CH2"
    ch3="CH3"
    all="all"

class IT63XX:
    def __init__(self,addr,model="IT6333A"):
        self.ser=serial.Serial(addr,9600,timeout=5)
        # self.ser.write("SYST:BEEP\r\n".encode("utf-8"))
        self.ser.write("*IDN?\r\n".encode("utf-8"))
        print(str(self.ser.readline()))
        self.ser.write("SYST:REM\r\n".encode("utf-8"))

    def channel_on(self,channel:supply_channel_number=supply_channel_number.all):
        if(channel != supply_channel_number.all):
            cmd="INST:SEL "+channel.value+"\r\n"
            self.ser.write(cmd.encode("utf-8"))
            self.ser.write("SOUR:CHAN:OUTPUT ON\r\n".encode("utf-8"))
        else:
            self.ser.write("OUTP:STAT ON\r\n".encode("utf-8"))

    def channel_off(self,channel:supply_channel_number=supply_channel_number.all):
        if(channel != supply_channel_number.all):
            cmd="INST:SEL "+channel.value+"\r\n"
            self.ser.write(cmd.encode("utf-8"))
            self.ser.write("SOUR:CHAN:OUTPUT OFF\r\n".encode("utf-8"))
        else:
            self.ser.write("OUTP:STAT OFF\r\n".encode("utf-8"))

    def set_voltage(self,channel:supply_channel_number,voltage:float):
        if(channel!=supply_channel_number.all):
            cmd="INST:SEL "+channel.value+"\r\n"
            self.ser.write(cmd.encode("utf-8"))
            cmd="SOUR:VOLT "+str(voltage)+"\r\n"
            self.ser.write(cmd.encode("utf-8"))

    def set_current(self,channel:supply_channel_number,current:float):
        if(channel!=supply_channel_number.all):
            cmd="INST:SEL "+channel.value+"\r\n"
            self.ser.write(cmd.encode("utf-8"))
            cmd="SOUR:CURR "+str(current)+"\r\n"
            self.ser.write(cmd.encode("utf-8"))

    def meas_voltage(self,channel:supply_channel_number):
        if(channel!=supply_channel_number.all):
            cmd="INST:SEL "+channel.value+"\r\n"
            self.ser.write(cmd.encode("utf-8"))
            cmd="MEAS:VOLT?\r\n"
            self.ser.write(cmd.encode("utf-8"))
            return float(self.ser.readline().decode().replace("\n",""))

    def meas_current(self,channel:supply_channel_number):
        if(channel!=supply_channel_number.all):
            cmd="INST:SEL "+channel.value+"\r\n"
            self.ser.write(cmd.encode("utf-8"))
            cmd="MEAS:CURR?\r\n"
            self.ser.write(cmd.encode("utf-8"))
            return float(self.ser.readline().decode().replace("\n",""))
            
    def beep(self):
        self.ser.write("SYST:BEEP\r\n".encode("utf-8"))

if __name__ == "__main__":
    my_supply=IT63XX("/dev/ttyS0")
    my_supply.channel_off()
    my_supply.channel_on(supply_channel_number.ch1)
    time.sleep(1)
    my_supply.set_voltage(supply_channel_number.ch1,12.345)
    # my_supply.meas_voltage(supply_channel_number.ch1)
    # my_supply.channel_off()
    # time.sleep(2)
    # my_supply.meas_current(supply_channel_number.ch1)