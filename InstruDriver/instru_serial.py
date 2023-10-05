import serial

class instru_socket(serial.Serial):

    def ask(self,cmd):
        self.write((cmd).encode("utf-8"))
        return(self.readline().decode())
        
    def write(self,cmd):
        self.write((cmd).encode("utf-8"))