import sqlite3 as sql

from DB_manager import sqlite_file

def show_all_cookies():
    pass
    ###


def addCookieToCart(cookieName):
    conn = sql.connect(sqlite_file)
    c = conn.cursor()
    c.execute('''INSERT INTO cart(item_id) VALUES (?)''', (cookieName,))
    conn.commit()
    conn.close()

def cartItems():
    conn = sql.connect(sqlite_file)
    c = conn.cursor()
    c.execute("SELECT item_id FROM cart")
    cart_Book_id = c.fetchall()
    cookie_Cart = []
    for cookie in cart_Book_id:
        c.execute("Select name, cost, cookies.id From cookies INNER JOIN cart on cart.item_id = cookies.id WHERE cookies.id LIKE ?", (cookie))


    cookiePrx = c.fetchall()
    cookie_Cart += cookiePrx
    conn.commit()
    conn.close()
    return cookie_Cart

def cartList():
    con = sql.connect(sqlite_file)
    c = con.cursor()
    c.execute("Select item_id from cart")
    cartCookieID = c.fetchall()
    cartLists= []
    for cookie in cartCookieID:
        cartLists.append(cookie[0])
    return cartLists
