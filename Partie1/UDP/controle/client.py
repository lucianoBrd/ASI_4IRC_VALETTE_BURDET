#!/usr/bin/env python

import socket

msgClient = "Hello Server"
msgToSend = str.encode(msgClient)
addrPort = ("127.0.0.1", 9999)
bufferSize = 1024

# Créer un socket UDP coté client
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while(True):
# Envoyer au serveur à l'aide du socket UDP créé
    str_input = str.encode(input("entrer start ou stop pour lancer l'application : "))
    s.sendto(str_input, addrPort)

