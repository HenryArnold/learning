from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'
@app.route('/login',method=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error render_template('login.html',error=error)
        do_the_login()
    else:
        show_the_login_form()
@app.route('/user/<username>')
def show_user_profile(username):
    #show the user profile for that user
    return 'user %s' %username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    #show the post with the given id, the id is an integer
    return 'post %d' %post_id
if __name__ == '__main__':
    app.run(debug = True)
