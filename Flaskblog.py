from flask import Flask, flash, redirect, render_template, request, url_for
from forms import RegistrationForm, LoginForm, SearchTicker
import os
from trade import searchStocks

app = Flask(__name__)

picFolder = os.path.join('static', 'Pictures')

app.config['SECRET_KEY'] = '035f8bff65ee4a394c36a0e11d01661f'
app.config['UPLOAD_FOLDER'] = picFolder

posts = [
     {
          'author': 'Kitty Cai, Richard Yang, Hugh Jiang, Fahim Ahmed',
          'title': 'How it Works',
          'content': 'Welcome to the Front-end of our hackathon project!',
          'date_posted': 'August 1, 2021'
     },
     {
          'author': 'Jane Doe',
          'title': 'Blog Post 2',
          'content': 'Second post content',
          'date_posted': 'April 21, 2018'
     },
]


@app.route("/")
@app.route("/home")
def home():
     search = SearchTicker(request.form)
     if request.method == 'POST':
          return search_results(search)
     StockMarket = os.path.join(app.config['UPLOAD_FOLDER'], 'StockMarketBW.jpg')
     #return render_template('home.html', main_image = StockMarket)
     return render_template('home.html', posts=posts, main_image = StockMarket, form = search)
     #return render_template('home.html')

@app.route("/about")
def about():
     return render_template('about.html', title = 'About')

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
          if form.email.data == 'admin@blog.com' and form.password.data == 'password':
               flash('You have been logged in!', 'success')
               return redirect(url_for('home'))
          else:
               flash('Login Unsuccessful. Please check username and password', 'danger')
     return render_template('login.html', title = "Sign In", form = form)

@app.route('/searchresults')
def searchresults(search):
     results = []
     search_string = search.data['search']

     results = searchStocks(search_string)

     if not results:
          flash('No results found!')
          return redirect('/')
     else:
          #Return results
          return render_template('results.html', results = results)
if __name__ == '__main__':
     app.run(debug=True)