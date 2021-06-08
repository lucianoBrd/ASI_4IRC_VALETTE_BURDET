# FLASK

## Environnment virtuel

Lancer le venv à l'aide de la commande `source venv/bin/activate`

## Lancer l'application Flask

Pour cela il faut exécuter la commande `python3 run.py`
Puis il faut se connecter sur votre navigateur à l'url `http://127.0.0.1:5000`

## Schéma
```mermaid
graph TB

  subgraph "Flask"
  App[run.py] --> Run[App]
  Run --> Modules[Modules]
  Modules --> ImageFichier[image_fichier]
  Modules --> ImageGeneration[image_generation]
  Modules --> ImageUrl[image_par_url]
  Modules --> ImageStreaming[image_streaming]

  ImageFichier --> Static1[Static - images, css, js]
  ImageGeneration --> Static2[Static - images, css, js]
  ImageUrl --> Static3[Static - images, css, js]
  ImageStreaming --> Static4[Static - images, css, js]
  ImageFichier --> Templates1[Templates - html]
  ImageGeneration --> Templates2[Templates - html]
  ImageUrl --> Templates3[Templates - html]
  ImageStreaming --> Templates4[Templates - html]
  ImageFichier --> Route1[route - image_fichier.py]
  ImageGeneration --> Route2[route - image_generation.py]
  ImageUrl --> Route3[route - image_par_url.py]
  ImageStreaming --> Route4[route - image_streaming.py]
end
```