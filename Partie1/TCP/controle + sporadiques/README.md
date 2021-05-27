# TCP

Afin de communiquer en TCP via python il faut utiliser des ```socket```.
Vous pouvez retrouver différents exemple de script python permettant de communiquer en TCP.

## Client

En effet, le fichier ```bind_socket.py``` permet de comprendre facilement comment se connecter à un serveur TCP.
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

## Serveur
