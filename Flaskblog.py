from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
import os
app = Flask(__name__)

picFolder = os.path.join('static', 'Pictures')

app.config['SECRET_KEY'] = '035f8bff65ee4a394c36a0e11d01661f'
app.config['UPLOAD_FOLDER'] = picFolder

posts = [
     {
          'author': 'Kitty Cai, Richard Yang, Hugh Jiang, Fahim Ahmed',
          'title': 'Blog Post 1',
          'content': 'First post content',
          'date_posted': 'April 20, 2018'
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
     StockMarket = os.path.join(app.config['UPLOAD_FOLDER'], 'StockMarketBW.jpg')
     #return render_template('home.html', main_image = StockMarket)
     return render_template('home.html', posts=posts, main_image = StockMarket)
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

@app.route("/login")
def login():
     form = LoginForm()
     return render_template('login.html', title = "Sign In", form = form)

if __name__ == '__main__':
     app.run(debug=True)