'''
This script holds the different URLs that the application implements
'''
from flask import render_template, flash,  redirect, url_for
from app import app
from app.forms import LoginForm

#The homepage for the application
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Adam'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html',title='MBHome',user=user,posts=posts)


#The route for logging in a user
@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)