#liberaries
from flask import Flask, redirect, url_for, render_template
import time
from employee import employee_data

#main application
app = Flask(__name__)

#home route
@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', title='Home')

#about route
@app.route('/about')
def about_page():
    return render_template('about.html', title='About')

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

#checking number
@app.route('/check/<int:num>')
def check(num):
    return render_template('check.html', title = 'Check', num=num)

#data retrieval
@app.route('/employee')
def employee():
    return render_template('employee.html', title='Employee', employee_data=employee_data)

#managers retrieval
@app.route('/managers')
def managers():
    return render_template('managers.html', title='Managers', employee_data=employee_data)

#server run
if __name__ == '__main__':
    app.run(debug=True)
