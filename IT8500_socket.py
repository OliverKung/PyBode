class InstrumentInterface:
    debug = 0  # Set to 1 to see dumps of commands and responses
    length_packet = 26  # Number of bytes in a packet
    convert_current = 1e4  # Convert current in A to 0.1 mA
    convert_voltage = 1e3  # Convert voltage in V to mV
    convert_power   = 1e3  # Convert power in W to mW
    convert_resistance = 1e3  # Convert resistance in ohm to mohm
    to_ms = 1000           # Converts seconds to ms
    # Number of settings storage registers
    lowest_register  = 1
    highest_register = 25
    # Values for setting modes of CC, CV, CW, or CR
    modes = {"cc":0, "cv":1, "cw":2, "cr":3}
    def Initialize(self,port,baudrate=9600,addrress=0,eth_or_serial=0):
        if(eth_or_serial==1):
            print("Socket Control IT8500")
            # use socket protocol
        if(eth_or_serial==0):
            print("Serial Control IT8500")
            # use serial protocol
    def CommandProperlyFormed(self,cmd):
        # check if command is properly formed
        # Return 1 if command is properly formed, otherwise return 0.
        commands = (
            0x20, 0x21, 0x22, 0x23, 0x24, 0x25, 0x26, 0x27, 0x28, 0x29,
            0x2A, 0x2B, 0x2C, 0x2D, 0x2E, 0x2F, 0x30, 0x31, 0x32, 0x33,
            0x34, 0x35, 0x36, 0x37, 0x38, 0x39, 0x3A, 0x3B, 0x3C, 0x3D,
            0x3E, 0x3F, 0x40, 0x41, 0x42, 0x43, 0x44, 0x45, 0x46, 0x47,
            0x48, 0x49, 0x4A, 0x4B, 0x4C, 0x4D, 0x4E, 0x4F, 0x50, 0x51,
            0x52, 0x53, 0x54, 0x55, 0x56, 0x57, 0x58, 0x59, 0x5A, 0x5B,
            0x5C, 0x5D, 0x5E, 0x5F, 0x60, 0x61, 0x62, 0x63, 0x64, 0x65,
            0x66, 0x67, 0x68, 0x69, 0x6A, 0x6B, 0x6C, 0x12
        )
        if len(cmd)!=self.length_packet:
            print("Commande length = "+str(len(cmd))+"instead of "+str(self.length_packet))
            return 0
            # first check the length of command
        if ord(cmd[0])!=0xaa:
            print("First byte should be 0xaa")
            return 0
        if ord(cmd[1])==0xff:
            print("Address(Seconde) Byte cannot be oxff")
            return 0
