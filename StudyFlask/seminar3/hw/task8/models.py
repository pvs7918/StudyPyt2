from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    surname = db.Column(db.String(80), nullable=False)
    e_mail = db.Column(db.String(80), nullable=False, unique=True)
    pwd_hash = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'User({self.id}, {self.name}, {self.surname}, {self.e_mail})'
