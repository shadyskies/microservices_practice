from functools import wraps
from urllib import request

from flask import Flask, jsonify, abort, render_template, g, redirect, url_for
import os
import requests
import json
from flask_cors import CORS

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__,
            static_url_path='',
            static_folder='static',
            template_folder='templates'
            )

app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
CORS(app)


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/', methods=['GET'])
@login_required
def home():
    try:
        data = requests.get('http://172.17.0.1:8000/api/blogs/')
        data = data.json()
        print(data)
        return render_template('index.html', blogs=data)
    except requests.exceptions.ConnectionError:
        return ('Connection refused')


@app.route('/post/', methods=['GET', 'POST'])
def post():
    return render_template('post.html')


@app.route('/register/', methods=['GET','POST'])
def register():
    return render_template('register.html')


@app.route('/login/', methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
