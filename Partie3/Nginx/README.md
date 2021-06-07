# Deploy with Nginx and uWSGI

## Sommaire
1. Créer environnement virtuel Python
2. Paramétrer une application Flask
3. Configurer uWSGI
4. Créer un systemd Unit File
5. Configurer Nginx pour Proxy Requests

Les fichiers sont disponible dans le dossier ```Nginx```

## 1. Créer environnement virtuel Python

Dans le dossier de l'application (```Nginx```) :

```python3 -m venv myprojectenv```

```source myprojectenv/bin/activate```

## 2. Paramétrer une application Flask

```pip3 install wheel```

```pip3 install uwsgi flask```

Ajouter les fichiers dans le dossier de l'application (```Nginx```) :
* project.ini
* project.py
* project.sock

```sudo ufw allow 5000```

## 3. Configurer uWSGI

```uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app```

```deactivate```

## 4. Créer un systemd Unit File

```sudo touch /etc/systemd/system/project.service```

File : ```/etc/systemd/system/project.service```
```
[Unit]
Description=uWSGI instance to serve my project
After=network.target

[Service]
User=luciano
Group=www-data
WorkingDirectory=/home/luciano/Bureau/ASI/asi_4irc_valette_burdet/Partie3/Nginx
Environment="PATH=/home/luciano/Bureau/ASI/asi_4irc_valette_burdet/Partie3/Nginx/myprojectenv/bin"
ExecStart=/home/luciano/Bureau/ASI/asi_4irc_valette_burdet/Partie3/Nginx/myprojectenv/bin/uwsgi --ini project.ini

[Install]
WantedBy=multi-user.target
```

```sudo systemctl start project```
```sudo systemctl enable project```

Tester :
```sudo systemctl status project```

## 5. Configurer Nginx pour Proxy Requests

```sudo touch /etc/nginx/sites-available/project```

File : ```/etc/nginx/sites-available/project```
```
server {
    listen 80;
    server_name test.com www.test.com;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/luciano/Bureau/ASI/asi_4irc_valette_burdet/Partie3/Nginx/project.sock;
    }
}
```

```sudo ln -s /etc/nginx/sites-available/project /etc/nginx/sites-enabled```

```sudo nginx -t```

```sudo systemctl restart nginx```

```sudo ufw allow 'Nginx Full'```

Accéder sur navigateur :
```http://test.com```

Si besoin, modifier le fichier ```/etc/hosts``` :
```
127.0.0.1	test.com
```


Voir logs :
```sudo journalctl -u project```