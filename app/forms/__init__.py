from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    """formulário para login"""
    username = StringField('Nome Usuário', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')


def validate_username(username):
    user = User.query.filter_by(username=username.data).first()
    if user is not None:
        raise ValidationError('Por favor use um nome de usuário diferente.')


def validate_email(email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
        raise ValidationError('Por favor use um endereço de email diferente.')


class SigninForm(FlaskForm):
    """formulário para signing"""
    username = StringField('Nome Usuário', validators=[DataRequired()])
    user_email = StringField('Email Usuário', validators=[DataRequired(), Email()])
    password1 = PasswordField('Senha Usuário', validators=[DataRequired()])
    password2 = PasswordField('Reintroduza Senha', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Cadastrar')
