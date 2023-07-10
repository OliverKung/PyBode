from MSO5K import *
from SDG2000X import *
import numpy as np
import math
from tqdm import tqdm

my_osc=mso5k("192.168.31.32","MSO5072")
my_dsg=SDG2000X("192.168.31.24","SDG2042X")

freq_list=np.logspace(6,8,1000,endpoint = True)
print(freq_list)
with open('F:\SoftDev\Instruments\inststa\data\\bode_data.csv',"w") as f:
    for freq in tqdm(freq_list):
        my_dsg.set_sine_waveform(freq,0.2,2)    
        # print(my_osc.voltage(channel_number.CH1,wave_parameter.RMS))
        # print(my_osc.voltage(channel_number.CH2,wave_parameter.RMS))
        # print(my_osc.phase(channel_number.CH1,channel_number.CH2))
        my_osc.autoscale()
        time.sleep(0.01)
        voltage1=my_osc.voltage(channel_number.CH1,wave_parameter.RMS)
        voltage2=my_osc.voltage(channel_number.CH2,wave_parameter.RMS)
        phase=my_osc.phase(channel_number.CH1,channel_number.CH2)
        gain=20*math.log(voltage2/voltage1,10)
        f.write(str(freq)+","+str(voltage1)+","+str(voltage2)+","+str(gain)+","+str(phase)+"\r")
        # print(str(voltage1)+","+str(voltage2)+","+str(gain)+","+str(phase)+"\r")
    f.close()