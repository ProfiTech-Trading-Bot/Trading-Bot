#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021
#ProfiTech Hackathon

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, SelectField, DateField
from wtforms.validators import DataRequired, Length, Email, EqualTo
import datetime

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

class SearchTickerForm(FlaskForm):
     ticker = StringField('Enter a Stock Ticker from S&P 500:', validators=[DataRequired()])
     submit = SubmitField('Enter')

class HistoricalTestForm(FlaskForm):
     ticker = StringField('Enter a Stock Ticker from S&P 500:', validators=[DataRequired()])
     start_date = DateField('Start Date of Tweets (YYYY-MM-DD)', format="%Y-%m-%d", default=datetime.datetime.now())
     submit = SubmitField('Enter')