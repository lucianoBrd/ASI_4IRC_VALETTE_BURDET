# Deploy with Docker

## Sommaire
1. Simple
2. Nginx

Les fichiers sont disponible dans les dossiers ```Nginx``` et ```Simple```.

Si besoin, stopper tous les containers : 
```
sudo docker system prune
```

## 1. Simple

Dans le dossier ```Simple``` :

```
sudo docker build -t flask-simple .

sudo docker run --name flask-simple -d -p 8080:8080 flask-simple
```

Vous avez maintenant accès à l'application via l'URL suivante : ```localhost:8080```

## 2. Nginx

Dans le dossier ```Nginx``` :

```
sudo docker build -t flask .

sudo docker run --name flask -d -p 8080:8080 flask
```

Vous avez maintenant accès à l'application via l'URL suivante : ```localhost:8080```