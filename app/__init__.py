from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# importando bootstrap para o projecto
# from flask_bootstrap import Bootstrap

# definindo a instância do flask
# com as definicoes do projecto
app = Flask(__name__)

# definindo as configuracoes do projecto
# importando-as do modulo config
app.config.from_object(Config)

# definindo a instância que configurara
# o login do usuário
login = LoginManager(app)
login.login_view = 'login'

# definindo as configuracoes de db
# para o projecto
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# iniciando a instância do bootstrap
# Bootstrap(app=app)

from app import routes, models
