# UDP Controle


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

Puis, on envoie la donnée encodé 
```python
str_input = str.encode(input("entrer start ou stop pour lancer l'application : "))
s.sendto(str_input, addrPort)
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

Puis, on traite la donnée reçu
```python
addr = s.recvfrom(1024)
message = addr[0].decode(encoding='UTF-8',errors='strict')
address = addr[1]

if message == "start":
    print("Application lancée")
elif message == "stop":
    print("Application arrêtée")
```

En fonction de l'information reçu on simule le lancement ou l'arrêt d'une application