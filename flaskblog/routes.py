from flask import render_template, url_for, flash, redirect
#Imports the Registration and Login Forms from the forms.py
from flaskblog import app, db,bcrypt
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User,Post



posts = [
        {'author': 'Edgar Cuevas',
    'title': 'Wine Color Change',
    'content': 'I have decided to change the color scheme to make the GUI prettier' ,
    'date_posted': 'November 2, 2018'},
    {'author': 'Edgar Cuevas',
    'title': 'Blog Post 2',
    'content': 'Second post content',
    'date_posted': 'November 1, 2018'}

]

#routes the server to the home page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', posts=posts)


#routes the server to the about page
@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data, email= form.email.data, password = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash ('You have been logged in!', 'success')
            return redirect (url_for('index'))
        else:
            flash('Login Unsuccesfull. Please check usename and password', 'danger')
    return render_template('login.html', title='Login', form=form)
