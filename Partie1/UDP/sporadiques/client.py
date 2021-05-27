#!/usr/bin/env python

import socket


addrPort = ("127.0.0.1", 9999)
bufferSize = 1024

# Créer un socket UDP coté client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
    s.sendto(str.encode("."), addrPort)
    msgServer = s.recvfrom(bufferSize)[0].decode()
    
    print(msgServer)


