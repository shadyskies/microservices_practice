import requests
from flask import Flask, jsonify, abort, render_template, g, redirect, url_for, request

from forms import RegistrationForm, LoginForm
from flask_login import login_user, current_user, logout_user, login_required

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_cors import CORS
import os

app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sessions.sqlite3'
app.config['SECRET_KEY'] = "some-random-text-here"
CORS(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

@app.route('/', methods=['GET'])
def home():
    try:
        data = requests.get('http://172.17.0.1:8000/api/blogs/')
        data = data.json()
        print(data)
        return render_template('index.html', blogs=data)
    except requests.exceptions.ConnectionError:
        return ('Connection refused')


@app.route('/blog/', methods=['GET', 'POST'])
def blog_view():
    return render_template('post.html')


@app.route('/register/', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for(''))
    form = RegistrationForm()
    if form.validate_on_submit():
        data = {
            "username": form.username.data,
            "password": form.password.data,
            "email": form.email.data
        }
        response = requests.post("http://172.17.0.1:8000/api/register/", json=data)
        if response.status_code == 201:
            return redirect(url_for('login'))
        else:
            return render_template('register.html', form=form, message=response.content)
    return render_template('register.html', form=form)


@app.route('/login/', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        data = {
            "username": form.username.data,
            "password": form.password.data
        }
        response = requests.get("http://172.17.0.1:8000/api/login/", json=data)
        if response.status_code == 200:
            return redirect('')
        else:
            return render_template('login.html', form=form, message=response.content)
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
