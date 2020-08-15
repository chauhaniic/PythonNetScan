#Open Port Scan

from socket import *
from sys import *

target = argv[1]
#port = argv[2]

for i in range(1,5000):
    s =  socket(AF_INET,SOCK_STREAM)

    try:
        s.connect((target,i))
        print(i,"Port Open")
        s.close()
    except:
        print(i," Port is CLosed")
        s.close()

