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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    if request.method == 'POST':
        if request.form['Firstname'] and request.form['Lastname'] and request.form['Email'] and request.form[
            'password'] and request.form['confirm password']:
            user = User(request.form['Firstname'] and request.form['Lastname'] and request.form['Email'] and
                        request.form[
                            'password'] and request.form['confirm password'])
            return redirect[url_for('login')]
    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop(logged_in, None)
    return rediect(url_for('home'))

    # @app.route('/create_list',methods=['GET', 'POST'])
