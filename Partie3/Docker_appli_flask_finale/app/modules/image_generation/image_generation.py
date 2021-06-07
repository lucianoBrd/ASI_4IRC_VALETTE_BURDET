#-------------------------------------------------------------------------------------------------
#--------------------------------------------IMAGE GENERATION--------------------------------------------------
#-------------------------------------------------------------------------------------------------
import requests
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
import jinja2
import pandas as pd

image_generation = Blueprint('image_generation', __name__, template_folder='templates', static_folder='static', url_prefix='/image_generation')

app = Flask(__name__)

#--------------------------------------------UI--------------------------------------------------
@image_generation.route('/ui')
def image_generation_ui():
    return render_template('image_generation.html')

#--------------------------------------------API--------------------------------------------------
#@aci.route('/api/connexion', methods=['POST'])
#def auth_aci_post():
#    apic_hostname = request.form.get('hostname')



if __name__ == '__main__':
    app.run()

