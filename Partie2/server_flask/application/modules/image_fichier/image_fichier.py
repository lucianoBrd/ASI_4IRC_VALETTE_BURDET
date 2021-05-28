#-------------------------------------------------------------------------------------------------
#--------------------------------------------IMAGE FICHIER--------------------------------------------------
#-------------------------------------------------------------------------------------------------
import requests
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
import jinja2
import pandas as pd

image_fichier = Blueprint('image_fichier', __name__, template_folder='templates', static_folder='static', url_prefix='/image_fichier')

app = Flask(__name__)

#--------------------------------------------UI--------------------------------------------------
@image_fichier.route('/ui')
def image_fichier_ui():
    return render_template('image_fichier.html')

#--------------------------------------------API--------------------------------------------------
#@aci.route('/api/connexion', methods=['POST'])
#def auth_aci_post():
#    apic_hostname = request.form.get('hostname')



if __name__ == '__main__':
    app.run()

