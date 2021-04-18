from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(130))

    def __init__(self, name, email, password):
        self.username = name
        self.email = email
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __getattr__(self, item: str = None):
        if item == 'username':
            return self.username
        elif item == 'email':
            return self.email
        elif item == 'password':
            return self.password_hash
        elif item is None:
            return {'username': self.username, 'email': self.email, 'password_hash': self.password_hash}
        else:
            pass

    def __repr__(self):
        return f"<User {self.username}>"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"<Post {self.body}>"


@login.user_loader
def load_user(_id):
    return User.query.get(int(_id))
