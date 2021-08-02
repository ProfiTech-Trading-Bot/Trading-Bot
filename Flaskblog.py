#Fahim Ahmed, Hugh Jiang, Richard Yang, Zhi Rong Cai
#July 31st, 2021 - August 2nd, 2021
#ProfiTech Hackathon

from stock_price import getTrend
from sentimental_analysis import TweetAnalyzer
from flask import Flask, flash, redirect, render_template, request, url_for
from forms import RegistrationForm, LoginForm, SearchTickerForm
import os
from trade import searchStocks

app = Flask(__name__)

picFolder = os.path.join('static', 'Pictures')

app.config['SECRET_KEY'] = '035f8bff65ee4a394c36a0e11d01661f'
app.config['UPLOAD_FOLDER'] = picFolder

# Create TweetAnalyzer object for use in trading()
tweetAnalyzer = TweetAnalyzer()

posts = [
     {
          'author': 'Kitty Cai, Richard Yang, Hugh Jiang, Fahim Ahmed',
          'title': 'How it Works',
          'content': 'Welcome to the Front-end of our hackathon project!',
          'date_posted': 'August 1, 2021'
     },
     {
          'author': 'Kitty Cai, Richard Yang, Hugh Jiang, Fahim Ahmed',
          'title': 'Meet the Profiters',
          'content': 'Take a glimpse of the Profiters who created the program!',
          'date_posted': 'August 1, 2021'
     }
]


@app.route("/")
@app.route("/home")
def home():
     search = SearchTickerForm(request.form)
     if request.method == 'POST':
          return search(search)
     StockMarket = os.path.join(app.config['UPLOAD_FOLDER'], 'StockMarketBW.jpg')
     #return render_template('home.html', main_image = StockMarket)
     return render_template('home.html', posts = posts, main_image = StockMarket, form = search)
     #return render_template('home.html')

@app.route("/about")
def about():
     Formatting = os.path.join(app.config['UPLOAD_FOLDER'], 'Formatting.jpg')
     return render_template('about.html', title = 'How it Works', formatimage = Formatting)

@app.route("/meet")
def meet():
     return render_template('meet.html', title = 'Meet the Profiters')

@app.route("/register", methods = ['GET', 'POST'])
def register():
     form = RegistrationForm()
     if form.validate_on_submit():
          flash(f'Account created for {form.username.data}!', 'success')
          return redirect (url_for('home'))
     return render_template('register.html', title = "Sign Up", form = form)

@app.route("/login", methods = ['GET', 'POST'])
def login():
     form = LoginForm()
     if form.validate_on_submit():
          if form.email.data == 'admin@gmail.com' and form.password.data == 'password':
               flash('You have been logged in!', 'success')
               return redirect(url_for('home'))
          else:
               flash('Login Unsuccessful. Please check username and password', 'danger')
     return render_template('login.html', title = "Sign In", form = form)

@app.route('/livesignals', methods=['GET', 'POST'])
def livesignals():
     form = SearchTickerForm()

     # Trade data that is passed to html template
     trade_data = {}

     # Check if the search input ticker is a valid ticker
     print(form.ticker)
     print(type(form.ticker.data))
     print(str(form.ticker.data))
     
     input = form.ticker.data
     
     # Check if an input was entered
     if input != None: 
          input = input.upper()

          if searchStocks(input) == False:
               flash(f'{input} is not a valid ticker symbol in the S&P500. Please try again.', 'error')
          else:

               currentTrend = 'uptrend' if getTrend(input) else 'downtrend'
               sentiment = tweetAnalyzer.getStockSentiment(input)
               
               if sentiment > 0 and currentTrend == 'uptrend':
                    status = 'BUY'
               elif sentiment < 0 and not currentTrend:
                    status = 'SELL'
               else:
                    status = 'ANALYSIS INCONCLUSIVE'

               trade_data = {
                    'ticker': input,
                    'trend': currentTrend,
                    'sentiment': sentiment,
                    'status': status
               }

     return render_template('livesignals.html', form=form, trade_data=trade_data)

if __name__ == '__main__':
     app.run(debug=True)