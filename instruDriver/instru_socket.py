import socket

class instru_socket(socket.socket):

    # def ask(self,cmd):
    #     self.send((cmd+"\r\n").encode("utf-8"))
    #     msg=self.recv(1024).decode()
    #     while(msg.find("\n")==False):
    #         msg+=self.recv(1024).decode()
    #     return(msg)

    def ask(self,cmd):
        self.send((cmd+"\r\n").encode("utf-8"))
        msg=self.recv(1024).decode()
        return(msg)
        
    def write(self,cmd):
        self.send((cmd+"\r\n").encode("utf-8"))
    