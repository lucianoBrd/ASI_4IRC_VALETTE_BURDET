#-------------------------------------------------------------------------------------------------
#--------------------------------------------IMAGE STREAMING--------------------------------------------------
#-------------------------------------------------------------------------------------------------
import requests
from flask import Flask, Blueprint, render_template, redirect, url_for, request, flash, session
import jinja2
import pandas as pd

image_streaming = Blueprint('image_streaming', __name__, template_folder='templates', static_folder='static', url_prefix='/image_streaming')

app = Flask(__name__)

#--------------------------------------------UI--------------------------------------------------
@image_streaming.route('/ui')
def image_streaming_ui():
    return render_template('image_streaming.html')

#--------------------------------------------API--------------------------------------------------
#@aci.route('/api/connexion', methods=['POST'])
#def auth_aci_post():
#    apic_hostname = request.form.get('hostname')



if __name__ == '__main__':
    app.run()

