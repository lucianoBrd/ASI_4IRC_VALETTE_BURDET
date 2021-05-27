# TCP Controle et Sporadiques

## Sommaire
1. Client
2. Serveur

Afin de communiquer en TCP via python il faut utiliser des ```socket```.
Vous pouvez retrouver différents exemple de script python permettant de communiquer en TCP.

## 1. Client

Le fichier ```bind_socket.py``` permet de comprendre facilement comment se connecter à un serveur TCP.
En outre, il faut dans un premier temps créer la ```socket``` :
```
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Ensuite, il faut définir le ```port``` et le ```host``` du serveur sur lequel nous souhaitons nous connecter :
```
host = 'www.google.com'
port = 80
```

Puis, il faut récupérer l'adresse IP du serveur :
```
remote_ip = socket.gethostbyname( host )
```

Enfin, nous pouvons nous connecter :
```
s.connect((remote_ip , port))
```

De plus, vous pouvez également trouver le fichier ```socket_client.py```. Ce srcipt permet de se connecter en TCP à un serveur et de lui envoyer un message comme des remontés de capteur, informations de contrôle...
En somme, une fois connecté au serveur, il suffit de faire comme ci-dessous pour envoyer puis recevoir un message :
```
s.sendall(message)
reply = s.recv(4096)
```

## 2. Serveur

Il y a différents exemple de fichiers de serveur TCP :
* ```socket_server.py``` est un exemple simple de fichier de serveur. 
* ```socket_server_with_select.py``` est un serveur pouvant accepter plusieurs clients.
* ```socket_server_threads.py``` est un serveur pouvant accepter plusieurs clients et utilisant des ```threads```.

Il faut dans un premier temps créer la ```socket``` :
```
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
```

Ensuite, il faut définir le ```port``` et le ```host``` du serveur :
```
HOST = '127.0.0.1'
PORT = 8888	
```

Par la suite, il faut ```bind``` la ```socket``` afin d'assigner le ```port``` et le ```host``` :
```
s.bind((HOST, PORT))
```

Puis, nous écoutons la ```socket``` :
```
s.listen(10)
```

Enfin, nous sommes prêt à accepter les clients :
```
conn, addr = s.accept()
```

De plus, pour recevoir puis envoyer un message il suffit de faire comme suit :
```
data = sock.recv(RECV_BUFFER)
sock.send('OK ... ' + data)
```