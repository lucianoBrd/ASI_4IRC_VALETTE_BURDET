# UDP sporadiques


## 1. Client

Le fichier ```client.py``` permet de se connecter à un server UDP
En outre, il faut dans un premier temps créer la ```socket``` :
```python
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

Ensuite, on défini l'IP et le port 
```python
addrPort = ("127.0.0.1", 9999)
```

Puis, on receptionne la donnée du server (si on appuie sur la touche entrée)
```python
s.sendto(str.encode("."), addrPort)
msgServer = s.recvfrom(bufferSize)[0].decode()
print(msgServer)
```

## 2. Serveur
Le fichier ```server.py``` permet de se connecter à un server UDP
En outre, il faut dans un premier temps créer la ```socket``` :
```python
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
```

Ensuite, on défini l'IP et le port 
```python
addrPort = ("127.0.0.1", 9999)
```

Puis, on envoie un signal au server si on appuie sur la touche entrée
```python
addr = s.recvfrom(1024)
    address = addr[1]

    print("\rpress enter to simulte bumper on this server")
    bumper = input("\r") #funtion bloquante donc on passe à la suite si on appuie sur Entrée
    msg = str.encode("ON")
    # remonté de l'information : le bumper a été activé
    s.sendto(msg, address)
```

En fonction de l'information reçu on simule le lancement ou l'arrêt d'une application