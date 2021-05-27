#!/usr/bin/env python

import socket



# Créer une socket datagramme
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Lier à l'adresse IP et le port
s.bind(("127.0.0.1", 9999))


# Écoutez les datagrammes entrants
while(True):
    addr = s.recvfrom(1024)
    address = addr[1]

    print("\rpress enter to simulte bumper on this server")
    bumper = input("\r") #funtion bloquante donc on passe à la suite si on appuie sur Entrée
    msg = str.encode("ON")
    # remonté de l'information : le bumper a été activé
    s.sendto(msg, address)