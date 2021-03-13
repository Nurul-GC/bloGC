from app import *
from app.forms import LoginForm, SigninForm
from flask import flash, redirect, render_template


@app.route('/')
@app.route('/index')
def index():
    form = LoginForm()
    return render_template("index.html", title='Angolackers', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Login requested for user {form.username.data}, remember_me={form.remember_me.data}
        flash(f'Bem-Vindo de volta {form.username.data}...')
        return redirect('/')
    elif form.username != None:
        flash(f'Relaxa {form.username.data} já tens a sessão iniciada...')
        return redirect('/')
    return render_template("login.html", title="Angolackers-InicioSessão", form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SigninForm()
    if form.validate_on_submit():
        # Signin requested for user {form.username.data}, remember_me={form.remember_me.data}
        flash(f'Bem-Vindo {form.username.data}, o seu cadastro foi bem sucedido...')
        return redirect('/')
    return render_template("signin.html", title="Angolacker-Cadastro", form=form)
