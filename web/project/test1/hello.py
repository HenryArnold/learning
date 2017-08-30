from flask import Flask, render_template, session, redirect, url_for
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guss string'
import os
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField 
from wtforms.validators import Required 

class NameForm(Form): 
    name = StringField('username', validators=[Required()]) 
    submit = SubmitField('Add')

class UserForm(form):
    users = StringField('users')
    submit = SubmitField('Delete')

#-----------------------------------
	
from flask_bootstrap import Bootstrap
from flask_script import Manager 
manager = Manager(app)

#-----------------------------------
#configure datebase
from flask_sqlalchemy import SQLAlchemy

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#-----------------------------------
###table form
@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm() 
    if form.validate_on_submit(): 
        user = User.query.filter_by(username=form.name.data).first()	
        if user is None: 
            user = User(username = form.name.data) 
            db.session.add(user) 
            session['known'] = False 
        else: 
            session['known'] = True 
        session['name'] = form.name.data 
        form.name.data = '' 
    if form1.validate_on_submit(): 
        user = User.query.filter_by(username=form1.users.data).first()
        if user is None: 
            user = User(username = form.users.data) 
            db.session.add(user) 
            session['known'] = False 
        else: 
            session['known'] = True 
        session['name'] = form1.users.data 
        form1.users.data = '' 
        return redirect(url_for('index'))
		
    return render_template('index.html', 
        form = form, form1 = form1 name = session.get('name'), 
        known = session.get('known', False))
    form1 = UserForm()
    if form1.	

@app.errorhandler(404) 
def page_not_found(e): 
    return render_template('404.html'), 404 
 
@app.errorhandler(500) 
def internal_server_error(e): 
    return render_template('500.html'), 500

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)
bootstrap = Bootstrap(app)


###database 
#model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer , primary_key=True)
    name = db.Column(db.String(64), unique=True)

    def __repr__(self):
        return '<Role %r>' % self.name
    users = db.relationship('User', backref='role') 
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(64), unique=True, index=True)
    password = db.Column(db.String(64), unique=False)	

    def __repr__(self): 
        return '<User %r>, <User %r>' % self.username , self.password
        
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
'''
#database initlize
###add username
db.create_all()
user_role = Role(name='User')
user = User(username = name, password = pwd, role=user_role)
db.session.add(user)
db.session.commit()
###modif username


class Account(Form):
    UserName = Role.query.all()
'''   

if __name__ == '__main__':
    manager.run()
    app.run(debug=True)
