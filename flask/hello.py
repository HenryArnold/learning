from flask import Flask, render_template, redirect, url_for, session
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guss string'

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, validators
from wtforms.validators import Required

from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

class loginForm(FlaskForm):
    userName = StringField(validators=[Required()])
    passWord = PasswordField(validators=[Required()])
    submit = SubmitField('login')
class registerForm(FlaskForm):
    submit = SubmitField('register')

#commit form
class commitForm(FlaskForm):
    userName = StringField(validators=[Required()])
    passWord = PasswordField(validators=[Required()]) 
    submit = SubmitField('register')
	
#delete user
class deleteForm(FlaskForm):
    submit = SubmitField('Delete')
class changeForm(FlaskForm):
    passWord = PasswordField( 'new password', [validators.Required()])
    submit = SubmitField('Modify')
	
#admin form
class queryForm(FlaskForm):
    account = StringField(validators=[Required()])
    submit = SubmitField('query')
    
#database query
from db import db, User

@app.route('/', methods=['GET', 'POST'])
def index():
    error = ""
    session['username'] = ''
    session['passWord'] = ''
    loginform = loginForm()
    register = registerForm()

    if loginform.validate_on_submit():
        if loginform.userName.data == 'root' and loginform.passWord.data == 'toor' :
            return redirect(url_for('admin'))
        else:
            user = User.query.filter_by(name = loginform.userName.data, password = loginform.passWord.data ).first()
            if user is None:
#edit error
                return redirect(url_for('index'))
            else:
                session['username'] = loginform.userName.data
                session['passWord'] = loginform.passWord.data
                loginform.userName.data = ''
                loginform.passWord.date = ''
                return redirect(url_for('user', username=session['username']))
    else:
        loginform.userName.data = ''
        loginform.passWord.data = ''
    if register.validate_on_submit():
        return redirect(url_for('register'))
    else:
        pass

    return render_template('login.html', form = loginform, form1 = register) 
	
@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    form3 = changeForm()
    form1 = deleteForm()
    user = User.query.filter_by(name = session['username']).first()
    pwd = user.password
    if form3.validate_on_submit():
        try:
            print(pwd)
            pwd = form3.passWord.data
            print(pwd)
            user.password = pwd
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user', username=user.name))
        except:
            print(pwd)
            pass 
    else:
        pass
    if form1.validate_on_submit():
        try:
            db.session.delete(user)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            return "error"
    else:
        pass


    return render_template('user.html', form2 = form3, form1 = form1, username=session['username'], passWord = pwd)
@app.route('/register', methods=['GET', 'POST'])
def register():
    form1 = commitForm()
    if form1.validate_on_submit():
        error = ""
        newUser = form1.userName.data
        newPwd = form1.passWord.data
        try:
            user = User(name = newUser, password = newPwd)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            error = "account have been registed"
            return redirect(url_for('register'))
    else:
        pass
    return render_template('register.html', form = form1)


@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form1 = queryForm()
    error = ''
    if form1.validate_on_submit():
        try:
            name = form1.account.data
            user = User.query.filter_by(name = name ).first()
            session['username'] = user.name
            return redirect(url_for('user', username=session['username']))
        except:
            error = "account is not exist"
            return redirect(url_for('admin'))

    else:
        pass
    return render_template('admin.html', form = form1, error = error)


if __name__ =='__main__':
    app.run(debug=True)
