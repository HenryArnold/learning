import os

from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session
app = Flask(__name__)

#config database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




#database model
class Account(db.Model):
    __tablename__ = 'accounts'
    id = db.Column(db.Integer, primary_key=True, index=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True)
    gender = db.Column(db.String(64), default="null")

    def __init__(self,  username, password, email):
        self.username = username
        self.password = password
        self.email = email

    def __repr__(self):
        return '<User %r>' %self.username
