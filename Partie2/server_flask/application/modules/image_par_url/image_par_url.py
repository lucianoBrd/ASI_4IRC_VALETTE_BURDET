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

@image_par_url.route('/uploads', methods=['GET', 'POST'])
def download():

    r = requests.get('https://www.google.com/images/srpr/logo11w.png')

    with open('application/modules/image_par_url/static/images/image1.png', 'wb') as f:
        f.write(r.content)
    return render_template('image_par_url.html')
if __name__ == '__main__':
    app.run()

