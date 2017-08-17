from app import app
from flask import render_template, redirect, url_for, request, session


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'Emma' or request.form['password'] != 'emma1234':
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


def signup():
    error = None
    if request.method == 'POST':
        if request.form['Firstname'] and request.form['Lastname'] and request.form['Email'] and request.form[
            'password'] and request.form['confirm password']:
            user = User(
                request.form['Firstname'] and request.form['Lastname'] and request.form['Email'] and request.form[
                    'password'] and request.form['confirm password'])
            return redirect[url_for('login')]
    return render_template('signup.html')
