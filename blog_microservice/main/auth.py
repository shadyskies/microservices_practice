from flask import Blueprint, render_template, redirect, url_for
auth = Blueprint('auth', __name__)

@auth.route('/register/', methods=['GET','POST'])
def register():
    return render_template('register.html')


@auth.route('/login/', methods=['GET','POST'])
def login():
    return render_template('login.html')

