# starting to determine routes
from flask import Flask,render_template
import DB_manager
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
    cookies = DB_manager.getAllCookies()
    return render_template('order.html', cookies=cookies)

@app.route('/save_order')
def save_order():
    return ('thanks for your order')



if __name__ == '__main__':
    app.run(debug=True) #kind of like the web server
#google flask template