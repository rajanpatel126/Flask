from flask_wtf import FlaskForm
from wtforms import (StringField, SelectField, DateField, PasswordField, SubmitField, BooleanField)
from wtforms.validators import (DataRequired, Length ,Email, Optional, EqualTo)


class SignupForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    gender = SelectField(
        'Gender',
        choices=[('M', 'Male'), ('F', 'Female')],
        validators=[Optional()]
    )
    dob = DateField(
        'Date of Birth',
        validators=[Optional()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=5, max=20)]
    )
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), Length(min=5, max=20), EqualTo('password')]
    )
    submit = SubmitField('Sign Up')
    
    
class LoginForm(FlaskForm):
    email = StringField(
        'Email',
        validators=[DataRequired(), Email()]
    )
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(min=5, max=20)]
    )
    remember_me = BooleanField('Remember Me')
    
    submit = SubmitField('Login')
    
    