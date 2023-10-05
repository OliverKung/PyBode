# MSO5000 Series Oscilloscope python vxi11 lib.
from enum import Enum

class interface_Enum(Enum):
    serial=0
    socket=1
    LXI=2