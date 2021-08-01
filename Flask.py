from flask import Flask, render_template
import os
app = Flask(__name__)

picFolder = os.path.join('static', 'Pictures')

app.config['UPLOAD_FOLDER'] = picFolder
''''
posts = {
     {
          'author': 'Corey Schafer',
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
}
'''

@app.route("/")
@app.route("/home")
def home():
     StockMarket = os.path.join(app.config['UPLOAD_FOLDER'], 'StockMarket.jpg')
     return render_template('home.html', main_image = StockMarket)
     #return render_template('home.html', posts=posts)
     #return render_template('home.html')

@app.route("/about")
def about():
     return render_template('about.html')

if __name__ == '__main__':
     app.run(debug=True)