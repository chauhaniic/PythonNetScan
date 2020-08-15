#TCP ECHO SERVER
from socket import *

host = "10.185.11.8"
port = 5454
s = socket(AF_INET,SOCK_STREAM)

s.bind((host,port))

s.listen(5)

while True:
	c,addr = s.accept()
	print("[+] Got connecting from ",addr)
	R_msg = c.recv(1024)
	print(R_msg.decode('ascii'))
	msg = "this is from server"
	c.send(msg.encode('ascii'))
	c.close()
