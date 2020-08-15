# Client for TCP Server
from socket import *

host = "10.185.11.8"
port = 5454
s = socket(AF_INET,SOCK_STREAM)

s.connect((host,port))

msg = "this is from Client"
s.send(msg.encode('ascii'))
R_msg = s.recv(1024)

print(R_msg.decode('ascii'))

s.close()
