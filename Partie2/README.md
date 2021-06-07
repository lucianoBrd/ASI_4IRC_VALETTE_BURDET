# 2 eme partie , approches microservices en python

```flask_cors```
Cette extension expose un décorateur simple pour décorer les routes **Flask**. Ajoutez simplement ```@cross_origin()``` sous un appel à l'incanation ```@app.route(..)``` de **Flask** pour accepter les options par défaut et autoriser ```CORS``` sur une route donnée.

```flask_socketio```
```Flask-SocketIO``` permet aux applications **Flask** d'accéder à des communications bidirectionnelles à faible latence entre les clients et le serveur. L'application côté client peut utiliser n'importe laquelle des bibliothèques clientes ****SocketIO** en **Javascript**, **Python**, **C++**, **Java** et **Swift**, ou tout autre client compatible pour établir une connexion permanente au serveur.

## Flask vs Bottle
Le principal avantage de **Flask** est qu'il a accès à une multitude de ressources en ligne à des fins de documentation.
De plus, ce que recommande Flask comme structure de prédilection, c'est son approche minimaliste qui ne perd pas de sa puissance. Il est simple à exécuter avec les fonctionnalités HTML ou bootstrap.
De plus, Flask est excellent pour créer des prototypes rapides grâce aux outils utiles inclus dans son package. Vous pouvez opter pour l'ORM ou le SQL, tandis que toutes les informations qui s'y rapportent sont disponibles dans la vaste documentation.

Bottle a pour principal avantage le processus de distribution à fichier unique. Cela signifie qu'il est simple de partager ou de télécharger l'application, car elle est essentiellement conçue comme un seul fichier Python. De plus, Bottle est assez flexible, car il comporte toutes les fonctionnalités nécessaires pour un site Web, telles que le routage ou la création de modèles.


## Flask vs Django
Avant d’insister sur leurs différences, soulignons tout de même que Flask et Django restent tous les deux des frameworks utilisables pour Python et sont dans l’ensemble assez similaires. Pour les deux, on retrouve la logique de la structure MVC. Il est donc assez simple de passer d’un framework à l’autre sans perdre ses repères.

Django est un framework Python full-stack et est développé « batteries included », (littéralement « piles incluses »), ce qui facilite à ses utilisateurs certaines taches communes de développement, comme l’authentification, le routage d’URL, ou encore la migration des schémas de base de données. Django accélère également le développement en fournissant des templates, un système ORM, et un outil de bootstraping.

Flask, quant à lui, est un framework simple, léger, minimaliste. Bien que Flask offre moins de fonctionnalités que Django, celui-ci facilite le développement et garantit une meilleure souplesse.

## Résumé
**Bottle** : plus petit framework autour (un seul fichier). Mieux vaut l'utiliser pour des tests jetables, de très petits sites, etc. Fanstastique pour enseigner et apprendre la programmation web.

**django** : framework python le plus connu. Vous pouvez faire à peu près tout avec, l'écosystème est fantastique (il existe une application Django tierce pour tout, c'est fou), mais il y a encore beaucoup à apprendre avant de pouvoir être productif avec. Utilisez-le si vous avez un site Web complexe à coder, avec beaucoup de logique personnalisée. Vous devrez l'apprendre à la fin si vous voulez être sérieux au sujet de la programmation Web en python.

**flask** : la taille est entre django et bottle. Bon pour les petits et moyens sites. Est maintenant assez bien équipé avec de nombreux plugins tiers. Utilisez-le lorsque vous souhaitez créer un site avec des fonctionnalités personnalisées mais que vous ne voulez pas charger tout le django.

**wep2py** : essayez de rivaliser avec django ET flask, mais propose une philosophie différente et comprend de nombreux outils graphiques.

**cherrypy** : un framework WSGI Python pur avec des performances très correctes sans rien ajouter. Mais maintenant que son serveur est disponible pour être utilisé séparément, je recommanderais d'utiliser simplement bottle/flask/django avec le serveur et d'oublier sa partie cadre car elle est très verbeuse.

**pyramid** : concurrent le plus fort de Django en terme de fonctionnalités, il est beaucoup moins monolithique et beaucoup plus flexible. Vous avez le contrôle. Cependant, l'intégration des composants django facilite les choses, la doc est meilleure et l'écosystème est bien plus grand. Alors je préfère Django. Mais vous pouvez faire tout ce que Django fait avec pyramide, c'est une question de goût.

**twisted** : framework Internet asynchrone. Vous avez bien lu : framework INTERNET, pas framework WEB. Vous pouvez faire du HTTP, bien sûr, mais aussi SSH, IMAP, FTP et bien plus encore. Le framework le plus puissant de tous, des performances incroyables et l'API la plus délicate à prendre en main.

**tornado** : framework web asynchrone. En gros le seul concurrent actuel de nodejs en pur Python (donc pas de gevent, pas d'extension, etc). L'API n'est pas fantastique, mais pas trop compliquée et les perfs sont bonnes. Websocket fonctionne immédiatement.

**webpy** : très vieux. Utilisez-le uniquement si vous aimez sa syntaxe qui donne l'impression que vous parlez HTTP directement, mais avec un joli wrapper Python.