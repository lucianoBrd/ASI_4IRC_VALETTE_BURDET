from flask import Flask


app = Flask(__name__)

# blueprint for non-auth parts of app
from .home import home as home_blueprint
app.register_blueprint(home_blueprint)

from .modules.image_par_url.image_par_url import image_par_url as image_par_url_blueprint
app.register_blueprint(image_par_url_blueprint)

from .modules.image_generation.image_generation import image_generation as image_generation_blueprint
app.register_blueprint(image_generation_blueprint)

from .modules.image_fichier.image_fichier import image_fichier as image_fichier_blueprint
app.register_blueprint(image_fichier_blueprint)

from .modules.image_streaming.image_streaming import image_streaming as image_streaming_blueprint
app.register_blueprint(image_streaming_blueprint)


