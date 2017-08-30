import os
#config database
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, session

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)




#database model
class User(db.Model):
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64), unique=False)

    def __init__(self, name, password):
        self.name = name
        self.password = password

    def __repr__(self):
        return '<User %r>' %self.name 
