from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from flask_login import LoginManager

# definindo a instância do flask
# com as definições do projecto
app = Flask(__name__)

# definindo as configurações do projecto
# importando-as do modulo config
app.config.from_object(Config)

# definindo a instância que configurara
# o login do usuário
login = LoginManager(app)
login.login_view = 'login'

# definindo as configurações de db
# para o projecto
db = SQLAlchemy(app)
migrate = Migrate(app, db)

manager = Manager(app=app)
manager.add_command('db', MigrateCommand)

# iniciando a instância do bootstrap
# Bootstrap(app=app)

from app import routes, models
