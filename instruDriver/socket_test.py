from instru_socket import *

ip_socket=instru_socket()
ip_socket.connect(("127.0.0.1",65506))
while(True):
    cmd=input()
    if(cmd=="exit"):
        break
    print((cmd+"\r\n").encode())
    print(ip_socket.ask(cmd))
    print(ip_socket.ask(""))