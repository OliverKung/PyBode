from distutils.command.clean import clean
from pydoc import cli
import socket
import time

client=socket.socket()
client.connect(("192.168.2.204",14415))
client.send("CH5\r".encode())
time.sleep(1)
print("CH4")
client.send("CH4\r".encode())
time.sleep(1)
print("CH3")
client.send("CH3\r".encode())
time.sleep(1)
print("CH2")
client.send("CH2\r".encode())
time.sleep(1)
print("CH1")
client.send("CH1\r".encode())
# data=client.recv(1024)
# print(data.decode())
client.close()