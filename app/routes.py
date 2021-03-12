from app import *
from app.forms import LoginForm
from flask import flash, redirect, render_template
from flas


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", title='Angolackers')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Login requested for user {form.username.data}, remember_me={form.remember_me.data}
        flash(f'Ola {form.username.data}...')
        return redirect('/')
    return render_template('login.html', title='Angolackers-login', form=form)
