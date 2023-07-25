from MSO5K import *
from SDG2000X import *
import argparse

class channelSet():
    def __init__ (self,osc_addr,afg_addr,args):
        self.osc = mso5k(osc_addr,"MSO5072")
        self.afg = SDG2000X(afg_addr,"SDG2000X")
        self.args = args
    def run(self):
        self.osc.setChannelAtte(channel_number.ch1,args.osc_ch1_atte)
        self.osc.setChannelAtte(channel_number.ch2,args.osc_ch2_atte)
        self.osc.setChannelAtte(channel_number.ch3,args.osc_ch3_atte)
        self.osc.setChannelAtte(channel_number.ch4,args.osc_ch4_atte)

        self.osc.setChannelUnit(channel_number.ch1,args.osc_ch1_unit)
        self.osc.setChannelUnit(channel_number.ch2,args.osc_ch2_unit)
        self.osc.setChannelUnit(channel_number.ch3,args.osc_ch3_unit)
        self.osc.setChannelUnit(channel_number.ch4,args.osc_ch4_unit)

        self.afg.setChannelLoadImpedance(channel_number.ch1,args.afg_ch1_load)
        self.afg.setChannelLoadImpedance(channel_number.ch2,args.afg_ch2_load)
        
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--afg-ip",type=str,default="",required=True,help="IP addr of function generator")
    parser.add_argument("--osc-ip",type=str,default="",required=True,help="IP addr of oscilliscope")
    parser.add_argument("-o1a","--osc-ch1-atte",type=str,default="1",help="osc channel1 atte ratio")
    parser.add_argument("-o2a","--osc-ch2-atte",type=str,default="1",help="osc channel2 atte ratio")
    parser.add_argument("-o3a","--osc-ch3-atte",type=str,default="1",help="osc channel3 atte ratio")
    parser.add_argument("-o4a","--osc-ch4-atte",type=str,default="1",help="osc channel4 atte ratio")
    parser.add_argument("-o1u","--osc-ch1-unit",type=str,default="VOLT",help="osc channel1 unit")
    parser.add_argument("-o2u","--osc-ch2-unit",type=str,default="VOLT",help="osc channel2 unit")
    parser.add_argument("-o3u","--osc-ch3-unit",type=str,default="VOLT",help="osc channel3 unit")
    parser.add_argument("-o4u","--osc-ch4-unit",type=str,default="VOLT",help="osc channel4 unit")
    parser.add_argument("-a1l","--afg-ch1-load",type=str,default="HZ",help="afg channel1 load")
    parser.add_argument("-a2l","--afg-ch2-load",type=str,default="HZ",help="afg channel2 load")
    return parser.parse_args()

if __name__=="__main__":
    args = parse_args()
    #arguments correction check
    uChannelSet=channelSet(args.osc_ip,args.afg_ip,args)
    uChannelSet.run()