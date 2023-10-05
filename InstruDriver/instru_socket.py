import socket

class instru_socket(socket.socket):

    def ask(self,cmd):
        self.send((cmd).encode("utf-8"))
        while(True):
            msg=self.recv(1024).decode()
            if(not msg):
                break
            else:
                msg_all+=msg
        return(msg_all)
        
    def write(self,cmd):
        self.send((cmd).encode("utf-8"))