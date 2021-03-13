from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):
    """formulario para login"""
    username = StringField('Nome Usuario', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class SigninForm(FlaskForm):
    """formulario para signin"""
    username = StringField('Nome Usuario', validators=[DataRequired()])
    useremail = StringField('Email Usuario', validators=[DataRequired(), Email()])
    password1 = PasswordField('Senha Usuario', validators=[DataRequired()])
    password2 = PasswordField('Reintroduza Senha', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Cadastrar')
