from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from app.models import User


class LoginForm(FlaskForm):
    """formulario para login"""
    username = StringField('Nome Usuario', validators=[DataRequired()])
    password = PasswordField('Senha', validators=[DataRequired()])
    remember_me = BooleanField('Lembrar-me')
    submit = SubmitField('Entrar')

class SigninForm(FlaskForm):
    """formulario para signin"""
    username = StringField('Nome Usuario', validators=[DataRequired()])
    user_email = StringField('Email Usuario', validators=[DataRequired(), Email()])
    password1 = PasswordField('Senha Usuario', validators=[DataRequired()])
    password2 = PasswordField('Reintroduza Senha', validators=[DataRequired(), EqualTo('password1')])
    submit = SubmitField('Cadastrar')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Por favor use um nome de usuario diferente.')
    
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Por favor use um endereço de email diferente.')
