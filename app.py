# starting to determine routes
from flask import Flask,render_template
# import DB_manager
import DB_orm

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
    cookies = DB_orm.getAllCookies()
    order_quantity = []#DB_manager.getQuantity()
    return render_template('order.html', cookies=cookies, order_quantity=order_quantity)

@app.route('/save_order')
def save_order():
    return ('thanks for your order')



if __name__ == '__main__':
    DB_orm.DB_setup()
    app.run(debug=True) #kind of like the web server
#google flask template