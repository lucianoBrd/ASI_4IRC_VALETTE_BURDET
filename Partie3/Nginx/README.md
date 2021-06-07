# Deploy with 

python3 -m venv myprojectenv

source myprojectenv/bin/activate

pip3 install wheel

pip3 install uwsgi flask

sudo ufw allow 5000

uwsgi --socket 0.0.0.0:5000 --protocol=http -w wsgi:app

deactivate


sudo touch /etc/systemd/system/project.service

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

sudo systemctl start project
sudo systemctl enable project

Tester :
sudo systemctl status project

sudo mkdir -p /etc/nginx/sites-available/
sudo touch /etc/nginx/sites-available/project

File : ```/etc/nginx/sites-available/project```
```
server {
    listen 80;
    server_name your_domain www.your_domain;

    location / {
        include uwsgi_params;
        uwsgi_pass unix:/home/luciano/Bureau/ASI/asi_4irc_valette_burdet/Partie3/Nginx/project.sock;
    }
}
```

sudo ln -s /etc/nginx/sites-available/project /etc/nginx/sites-enabled

sudo nginx -t

sudo systemctl restart nginx

sudo ufw allow 'Nginx Full'

sudo journalctl -u project