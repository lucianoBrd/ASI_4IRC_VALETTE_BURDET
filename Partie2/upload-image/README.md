# Microservices

## Sommaire
1. Serveur
2. Client

Afin de lancer les scripts, utiliser python 3. Par exemple :
```python3 server.py```

Ces scripts permettent de transférer un fichier en HTTP d'un navigateur au serveur. Il faut lancer d'abord le serveur puis nous pouvons accéder au navigateur.

## 1. Serveur

Initialiser l'application flask :
```
app = Flask(__name__)
```

Définir la route HTTP liée à une fonction python (en l'occurence POST dans l'exemple) :
```
@app.route('/', methods=['GET', 'POST'])
def upload_file():
```

Lancer l'application flask :
```
app.run(host="127.0.0.1", port=8888)
```

De plus, la fonction ```upload_file``` retourne si la méthode est ```GET``` le formulaire d'upload sinon si la méthode est ```POST``` la focntion enregistre le fichier reçu.

## 2. Navigateur

Accéder à la page suivante sur le navigateur :
```127.0.0.1:8888```