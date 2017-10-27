# starting to determine routes
from flask import Flask,render_template

app = Flask(__name__)

# @app.route('/')
# @app.route('/index.html')
@app.route('/', methods=['Get'])#route to home page
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/order')
def order():
    return render_template('order.html')



if __name__ == '__main__':
    app.run(debug=True) #kind of like the web server
#google flask template