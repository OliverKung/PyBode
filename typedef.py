from enum import Enum
class channel_number(Enum):
    CH1="CHAN1"
    ch1="CHAN1"
    CH2="CHAN2"
    ch2="CHAN2"
    CH3="CHAN3"
    ch3="CHAN3"
    CH4="CHAN4"
    ch4="CHAN4"

class wave_parameter(Enum):
    Peak2Peak = "VPP"
    peak2peak = "VPP"
    rms = "VRMS"
    RMS = "VRMS"
    AVG = "VAVG"
    avg = "VAVG"

class signal_generator_channel_number(Enum):
    CH1="1"
    ch1="1"
    CH2="2"
    ch2="2"

class waveform_type(Enum):
    dc = "DC"
    pulse = "PULS"
    ramp = "RAMP"
    sin = "SIN"
    square = "SQU"
    triangle = "TRI"
