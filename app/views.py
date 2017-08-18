from app import app
from flask import render_template, redirect, url_for, request, session, flash

from app.models.User import User
from app.models.application import Application

application = Application()


@app.route('/')
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        email_ = request.form['email']
        password_ = request.form['password']
        confirm_password_ = request.form['confirm_password']
        if email_ and password_ and confirm_password_:
            if password_ == confirm_password_:
                user = User(email_, password_)
                if application.create_user(user):
                    return redirect(url_for('login'))
            flash('your passwords do not match')
        error = 'Fill in the missing attributes'
    return render_template('signup.html', error=error)


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    error1 = None
    if request.method == 'POST':
        if request.form['email'] and request.form['password']:
            if application.login(request.form['email'], request.form['password']):
                # session['email'] = request.form['email']
                return redirect(url_for('home'))
            error = 'Invalid credentials. please try again.'
            return render_template('login.html', error=error)
        return render_template('login.html', error1=error1)
    return render_template('login.html')


@app.route('/home')
def home():
    return render_template('home.html')
