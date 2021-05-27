# TCP Flux

## Sommaire
1. Transfert de fichier
2. Transfert d'image

Afin de lancer les scripts, utiliser python 3. Par exemple :
```python3 client_file.py index.jpeg```

Si besoin installer la dépendance :
```pip3 install tqdm```

## 1. Transfert de fichier

Ces scripts permettent de transférer tout type de fichier d'un client au serveur TCP.
Il faut lancer le serveur puis le client :
```
python3 server_file.py
python3 client_file.py index.jpeg
```
Comme vous pouvez le constater il faut préciser le chemin de l'image au client.

## 2. Transfert d'image
Ces scripts permettent de transférer des images (exemple celle de la webcam) d'un client au serveur TCP.
```
python3 server_image.py
python3 client_image.py
```