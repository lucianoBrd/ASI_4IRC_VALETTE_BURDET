# Microservices

## Sommaire
1. Serveur
2. Client

Afin de lancer les scripts, utiliser python 3. Par exemple :
```python3 server.py```

Si besoin installer les dépendances :
* ```pip3 install jsonpickle```
* ```pip3 install flask```

Ces scripts permettent de transférer une image en HTTP d'un client au serveur. Il faut lancer d'abord le serveur puis le client.

## 1. Serveur

Initialiser l'application flask :
```
app = Flask(__name__)
```

Définir la route HTTP liée à une fonction python (en l'occurence POST dans l'exemple) :
```
@app.route('/api/test', methods=['POST'])
def test():
```

Lancer l'application flask :
```
app.run(host="127.0.0.1", port=8888)
```

## 2. Client

Préparer les ```headers``` pour pour la requête HTTP :
```
content_type = 'image/jpeg'
headers = {'content-type': content_type}
```

Récupérer et encoder l'image :
```
img = cv2.imread('index.jpeg')
_, img_encoded = cv2.imencode('.jpg', img)
```

Envoyer la requête HTTP :
```
response = requests.post(test_url, data=img_encoded.tostring(), headers=headers)
```