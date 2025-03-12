#liberaries
from flask import Flask, redirect, url_for
import time

#main application
app = Flask(__name__)

#home route
@app.route('/')
@app.route('/home')
def home_page():
    return '<h1>This is the first Flask application</h1>'

#about route
@app.route('/about')
def about_page():
    return '<h1>This is the about page</h1>'

#path parameters - dynamic URL
@app.route('/welcome/<name>')
def welcome_page(name):
    return f'<h1>Welcome {name.title()}!!</h1>'

#addition of two integers passed as path parameters
@app.route('/addition/<int:n1>/<int:n2>')
def addition(n1,n2):
    return f'<h1>Addition of {n1} and {n2} is {n1+n2}</h1>'

#URL redirection
@app.route('/marks/<name>/<int:num>')
def marks(name, num):
    if num < 33:
        time.sleep(1)
        return redirect(url_for('failed', name=name))
    else:
        time.sleep(1)
        return redirect(url_for('passed', name=name))

#if pass
@app.route('/pass/<name>')
def passed(name):
    return f'<h1>Congretulations {name.title()}!! You have passed</h1>'

#if fail
@app.route('/fail/<name>')
def failed(name):
    return f'<h1>Sorry {name.title()}!! You have failed</h1>'

#server run
if __name__ == '__main__':
    app.run(debug=True)
