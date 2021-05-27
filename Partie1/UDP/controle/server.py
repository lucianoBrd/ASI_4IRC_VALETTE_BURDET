#!/usr/bin/env python

import socket


# Créer une socket datagramme
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Lier à l'adresse IP et le port
s.bind(("127.0.0.1", 9999))
print("Serveur UDP à l'écoute")

# Écoutez les datagrammes entrants
while(True):
    addr = s.recvfrom(1024)
    message = addr[0].decode(encoding='UTF-8',errors='strict')
    address = addr[1]

    if message == "start":
        print("Application lancée")
    elif message == "stop":
        print("Application arrêtée")
