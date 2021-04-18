from flask import flash, redirect, render_template, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from app import *
from app.forms import LoginForm, SigninForm
from app.models import User


@app.route('/')
@app.route('/index')
@login_required
def index():
    try:
        return render_template("index.html", title='Angolackers-BloGC')
    except Exception as error:
        flash(f"{error}... 😥")
        return render_template("extrainfo.html", title='Angolackers-Erro')


@app.route('/about')
def about():
    return render_template("about.html", title="Angolackers-Sobre")


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    signinForm = SigninForm()
    if signinForm.validate_on_submit():
        user = User(name=signinForm.username.data, email=signinForm.user_email.data, password=signinForm.password1.data)
        sessao = db.create_session(user.__getattr__())
        sessao.add(user)
        sessao.commit()
        flash('Cadastro Foi Bem Sucedido, Agora inicie sessão para ter acesso a sua conta! 😉')
        return redirect(url_for('login'))
    return render_template("signin.html", title="Angolacker-Cadastro", form=signinForm)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        user = User.query.filter_by(username=loginForm.username.data).first()
        if user is None or not user.check_password(loginForm.password.data):
            flash('Nome de usuário ou Senha incorrectos... 😥')
            return redirect(url_for('signin'))
        flash(f'Inicio-Sessão Bem Sucedido, Bem-Vindo {loginForm.username.data}... 😄')
        login_user(user, remember=loginForm.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", title="Angolackers-InicioSessão", form=loginForm)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
