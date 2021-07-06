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