import requests
from flask import Flask, jsonify, abort, render_template, g, redirect, url_for, request

from forms import RegistrationForm, LoginForm, BlogCreateForm
from flask_login import login_user, current_user, logout_user, login_required
from app import app, db
from models import User


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


@app.route('/post-create/', methods=['GET', 'POST'])
@login_required
def create_blog():
    form = BlogCreateForm()
    if form.validate_on_submit():
        data = {
            "title": form.title.data,
            "content": form.content.data,
            "author": current_user.username
        }
        print(data)
        response = requests.post("http://172.17.0.1:8000/api/blogs/", json=data)
        if response.status_code == 200:
            return redirect(url_for(''))

    return render_template('create-blog.html', form=form)


@app.route("/post/<int:post_id>")
def post(post_id):
    response = requests.get(f'http://172.17.0.1:8000/api/blogs/{post_id}')
    return render_template('post.html', post=response.json())


@app.route('/register/', methods=['GET', 'POST'])
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
            res_data = response.json()
            user = User(id=res_data['id'], username=res_data['username'], password=res_data['password'], email=res_data['email'])
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
        else:
            return render_template('register.html', form=form, message=response.content)
    return render_template('register.html', form=form)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        data = {
            "username": form.username.data,
            "password": form.password.data
        }
        response = requests.post("http://172.17.0.1:8000/api/login/", json=data)
        if response.status_code == 200:
            user = User.query.filter_by(username=data['username']).first()
            login_user(user)
            return redirect('')
        else:
            return render_template('login.html', form=form, message=response.content)
    return render_template('login.html', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
