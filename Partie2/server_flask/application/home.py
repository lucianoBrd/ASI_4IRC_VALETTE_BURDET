from flask import Flask, render_template, Blueprint, request, redirect, url_for

home = Blueprint('home', __name__)

app = Flask(__name__)

@home.route('/')
def homepage():
    return render_template('home.html')


if __name__ == '__main__':
    app.run()

