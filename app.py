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
    #prices =  cookie.price

        #print(cookie.price)
    # order_total = [price[2] for price in order_quantity]
   # price = request.form['']
    #print(prices)
    for c in cookies:
        print(c)
    #cook_price = [price[2] for price in cookies]
    #print(cookies)
    print(order_quantity)
    return render_template('order.html', cookies=cookies)



@app.route('/order_saved', methods=['Post'])
def save_order():
    banana = request.args.get('cookie_type')
    bananas = request.args.get('quantity')
    DB_orm.add_order_to_db(banana, bananas)
    return render_template('order_saved.html', order=order)



if __name__ == '__main__':
    DB_orm.DB_setup()
    app.run(debug=True) #kind of like the web server
#google flask template