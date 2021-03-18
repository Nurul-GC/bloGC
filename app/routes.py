from app import *
from app.forms import LoginForm, SigninForm
from flask import flash, redirect, render_template
from flask_login import current_user, login_user
from app.models import User


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Angolackers')


@app.route('/about')
def about():
    return render_template("about.html", title="Angolackers-Sobre")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    loginForm = LoginForm()
    if loginForm.validate_on_submit():
        # Login requested for user {loginForm.username.data}, remember_me={loginForm.remember_me.data}
        flash(f'Bem-Vindo de volta {loginForm.username.data}...')
        return redirect('/')
    return render_template("login.html", title="Angolackers-InicioSessão", form=loginForm)


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    signinForm = SigninForm()
    if signinForm.validate_on_submit():
        # Signin requested for user {loginForm.username.data}, remember_me={loginForm.remember_me.data}
        flash(f'Bem-Vindo {signinForm.username.data}, o seu cadastro foi bem sucedido...')
        return redirect('/')
    return render_template("signin.html", title="Angolacker-Cadastro", form=signinForm)
