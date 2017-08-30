#init app
from flask import Flask, render_template, redirect, url_for, session, flash
"""
from flask.wtf import form
#test
from flaskext.wtf import Form
from wtforms_appengine.db import model_form
from mdels import MyModel
"""

app = Flask(__name__)


"""
#basical config
import config
app.BaseConfig()
"""
# 邮箱验证
#config csrf key
app.config['SECRET_KEY'] = 'hard to guss string'
"""
#configure smtp
from flask_mail import Mail, Message
mail = Mail(app)
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'xiaobaicaiabc@gmail.com'
app.config['MAIL_PASSWORD'] = 'WANGmima***'
app.config['MAIL_DEFAULT_SENDER'] = 'confirm message'
"""

#config Bootstrap
from flask_bootstrap import Bootstrap
bootstrap = Bootstrap(app)

#database config
from db import db, Account


# form Model
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, HiddenField, IntegerField, validators
from wtforms.validators import Required, EqualTo, Email

class loginForm(FlaskForm):
    userName = StringField(validators=[Required()])
    passWord = PasswordField(validators=[Required()])
    submit = SubmitField('login')

class registerForm(FlaskForm):
    userName = StringField(validators=[Required()])
    passWord = PasswordField(validators=[Required(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField(validators=[Required(), EqualTo('confirm', message='Passwords must match')])
    email = StringField(validators=[Required(), Email()])
    submit = SubmitField('register')

class deleteForm(FlaskForm):
    submit = SubmitField('Delete')

class changeForm(FlaskForm):
    passWord = PasswordField( 'new password', [validators.Required()])
    submit = SubmitField('Modify')

class queryForm(FlaskForm):
    account = StringField(validators=[Required()])
    submit = SubmitField('query')

# password vertify
def md5Pwd(password):
    import hashlib
    m = hashlib.md5()
    m.update(password.encode("utf-8"))
    return m.hexdigest()

    return(generate_password_hash('password', 12))
def checkPwd(pwd_hash, password):
    from flask_bcrypt import check_password_hash
    return (check_password_hash(pwd_hash, password))

"""
#generate token
from itsdangerous import URLSafeTimedSerializer
def generate_token(email):
    serializer = URLSafeTimedSerializer('my_precious')
    return serializer.dumps(email, salt='my_precious_two')

#confirm your email
def confirm_token(token, expiration=3600):
    serializer = URLSafeTimedSerializer(""""""sercret key """""")
    try:
        email = serializer.loads(token, salt=app.config['SECURITY_PASSWORD_SALT'], max_age= expiration )
    except:
        return False
    return email

#send email to vertify
def send_email(email, subject):
    token = generate_token(email)
    confrim_url = url_for('confirm_email', token=token, _external=True)
    html = render_template(email.html, confirm_url=confirm_url)
    msg = Message(subject, recipients=[email])
    msg.html
    mail.send(msg)
"""
#init database
from db import db, Account
db.drop_all()
db.create_all()
user1 = Account(username="test1", password=md5Pwd("test1"), email="test1@gmail.com")
user2 = Account(username="test2", password=md5Pwd("test2"), email="test2@gmail.com")
db.session.add_all([user1, user2])
db.session.commit()

#view function
@app.route('/', methods=['GET', 'POST'])
def index():
    session['username'] = ''
    session['passWord'] = ''
    loginform = loginForm()
    if loginform.validate_on_submit():
        if loginform.userName.data == 'root' and loginform.passWord.data == 'toor' :
            return redirect(url_for('admin'))
        else:
            password = loginform.passWord.data
            pwd = md5Pwd(password)
            user = Account.query.filter_by(username = loginform.userName.data, password = pwd ).first()
            if user is None:
                flash("username or password is error")
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
    return render_template('login.html', form = loginform, form1 = register)

@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    form3 = changeForm()
    form1 = deleteForm()
    user = Account.query.filter_by(username = session['username']).first()
    pwd = session['passWord']
    email = user.email
    if form3.validate_on_submit():
        try:
            pwd = form3.passWord.data
            session['passWord'] = pwd
            user.password = md5Pwd(pwd)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('user', username=user.username))
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
    return render_template('user.html', form2 = form3, form1 = form1, username=session['username'], password = pwd, email = email )
"""
@app.route('/user/edit')
def edit():
    myForm = model_form(myModel, Form)
    model = MyMdel.get()
    form = MyForm(request.form, model)

    if form.validate_on_submit():
        form.populate_obj(model)
        model.put()
        flash("MyModel updated")
        return redirect(url_for("index"))
    return render_template("edit.html", form=form)
"""
@app.route('/register', methods=['GET', 'POST'])
def register():
    form1 = registerForm()
    if form1.validate_on_submit():
        newUser = form1.userName.data
        newPwd = form1.passWord.data
        email = form1.email.data
        """
        #generate confirm url
        token = generate_token(email)
        confirm_url = confirm_token(token)
        # email vertify
        try:
            send_email(email, confirm_url , email.html)
        except:
            flash("email is not exit")
            return redirect(url_for('register'))
        """
        try:
            user = Account(username = newUser, password = md5Pwd(newPwd), email = email)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        except:
            flash(" username have been registered ")
            return redirect(url_for('register'))
    else:
        pass
    return render_template('register.html', form = form1)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    form1 = queryForm()
    users = Account.query.all()
    data = []
    for user in users:
        data1 = {}
        data1 = {
          "ID": user.id,
          "username": user.username,
          "password": user.password,
          "email": user.email,
          "gender": user.gender,
        }
        data.append(data1)
        columns = [
          {
            "field": "ID",
            "title": "ID",
            "sortable": True,
          },
          {
            "field": "username", # which is the field's name of data key
            "title": "username", # display as the table header's name
            "sortable": True,
          },
          {
            "field": "password",
            "title": "password",
            "sortable": True,
          },
          {
            "field": "email",
            "title": "email",
            "sortable": True,
          },
          {
            "field": "gender",
            "title": "gender",
            "sortable": True,
          }
        ]
    if form1.validate_on_submit():
        try:
            name = form1.account.data
            user = Account.query.filter_by(username = name ).first()
            session['username'] = user.username
            return redirect(url_for('user', username=session['username']))
        except:
            flash( "account is not exist" )
            return redirect(url_for('admin'))
    else:
        pass
    return render_template('admin.html', form = form1, data = data, columns = columns, title='Account Table')


if __name__ =='__main__':
    app.run(debug=True)
