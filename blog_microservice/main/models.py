from routes import db, login_manager
from flask_login import UserMixin


@login_manager.load_user
def load_user(user):
    return User.get(user)

