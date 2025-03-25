#liberaries
from flask import Flask, redirect, url_for, render_template, redirect, flash
import time
from employee import employee_data
from forms import SignupForm, LoginForm
from flask_sqlalchemy import SQLAlchemy


#main application
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees_db.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#database object
db = SQLAlchemy(app)

#tables are represented as classes
class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    age = db.Column(db.Integer, nullable=False)
    
    #to display the output we wanted
    def __repr__(self):
        return f'Employee(name={self.name}, email={self.email}, age={self.age}))'

#csrf token (random value)
app.config['SECRET_KEY'] = 'this_is_the_sceret_key'

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

#sign-up page
@app.route('/signup', methods=['GET','POST'])
def signup_page():
    form = SignupForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!')
        return redirect(url_for('home_page'))
    return render_template('signup.html', title='Sign-up', form=form)

#login page
@app.route('/login', methods=['GET','POST'])
def login_page():
    form = LoginForm()
    email = form.email.data
    pw = form.password.data
    if form.validate_on_submit():
        # hard coded values
        if email == "a@b.com" and pw == "12345":
            flash("Logged in Successfully!")
            return redirect(url_for("home_page"))
        else:
            flash("Incorrect email or password")
    return render_template('login.html', title='Login', form=form)

#server run
if __name__ == '__main__':
    app.run(debug=True)
