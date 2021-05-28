#-------------------------------------------------------------------------------------------------
#--------------------------------------------IMAGE PAR URL--------------------------------------------------
#-------------------------------------------------------------------------------------------------
import requests
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
import jinja2
import pandas as pd

image_par_url = Blueprint('image_par_url', __name__, template_folder='templates', static_folder='static', url_prefix='/image_par_url')

app = Flask(__name__)

#--------------------------------------------UI--------------------------------------------------
@image_par_url.route('/ui')
def image_par_url_ui():
    return render_template('image_par_url.html')

#--------------------------------------------API--------------------------------------------------
#@aci.route('/api/connexion', methods=['POST'])
#def auth_aci_post():
#    apic_hostname = request.form.get('hostname')



if __name__ == '__main__':
    app.run()

