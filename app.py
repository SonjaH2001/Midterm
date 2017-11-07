# starting to determine routes
from flask import Flask,render_template, request
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

@app.route('/order',  methods=['Get', 'Post'])
def order():
    cookies = DB_orm.getAllCookies()

    #var to hold cookie selection
    cookie_choice = request.form.get('cookie_type')

    #var to hold num of cookies
    order_quantity = request.form.get('quantity') #DB_manager.getQuantity()

    DB_orm.add_order_to_db(cookie_choice,order_quantity)
    return render_template('order.html', cookies=cookies)



@app.route('/order')
def save_order():
    return ('thanks for your order')



if __name__ == '__main__':
    DB_orm.DB_setup()
    app.run(debug=True) #kind of like the web server
#google flask template