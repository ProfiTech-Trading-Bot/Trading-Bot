from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
     #Makes sure the username is valid and has less than 20 characters but at least 2 characters
     username = StringField('Username', validators = [DataRequired(), Length(min = 2, max = 20)])

     email = StringField('Email', validators = [DataRequired(), Email()])

     password = PasswordField('Password', validators = [DataRequired()])
     confirmpassword = PasswordField('Confirm Password', validators = [DataRequired(), EqualTo('password')])

     submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
     email = StringField('Email', validators = [DataRequired(), Email()])

     password = PasswordField('Password', validators = [DataRequired()])

     remember = BooleanField('Remember Me')
     submit = SubmitField('Login')

class SearchTicker(FlaskForm):
     choices = ['TSLA', 'AAPL']
     select = SelectField('Search for stocks:', choices = choices)
     search = StringField('')