from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy import event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from base import *
# from sqlalchemy import *
# from sales import Sale
# from events import Event
from classes import Cookie, Orders
# import ui
# import classes

#from Jennifer Plemel
# engine = create_engine('sqlite:///:memory:', echo=False)
engine = create_engine('sqlite:///cookies_stuff.db', echo=False)

# Base = declarative_base() #All of the mapped classes inherit from this class
Base.metadata.create_all(engine)  # Create a table for all the classes that use Base

# '''Need a session to talk to the database'''
# A session manages mappings of objects to rows in the database
# Make a session class -- only need to do this one time
Session = sessionmaker(bind=engine)  # using the engine created earlier


def DB_setup():
    # engine = create_engine('sqlite:///:memory:', echo=False)


    setup_session = Session()

    cookie1 = Cookie(description = 'Seasonal Sensation', price = '4')
    cookie2 = Cookie(description = 'Sugar Hill Gang', price = '6')
    cookie3 = Cookie(description = 'Chocolate Pinky Delights', price = '3')
    cookie4 = Cookie(description = 'Chocolate Chip Peanut Butter Dream', price ='9')
    # Add cookie object to session -- this tells the session that you want to map
    # the cookie object to a row in the DB


    for item in [cookie1, cookie2, cookie3, cookie4]:
        if not (check_item(item.description)):
            # Add merch object to session -- this tells the session that you want to map
            # the merch object to a row in the DB
            setup_session.add(item)
    #saves when committed and closed
    setup_session.commit()
    all_cookies = setup_session.query(Cookie).all()
    print((all_cookies))
    setup_session.close()

def check_item(string):
    check_session = Session()
    count_item = check_session.query(Cookie).filter_by(description=string).count()
    if (count_item > 0):
        check_session.close()
        return True
    else:
        check_session.close()
        return False

    # check_session.close()
    # item_exists = count_item > 0
    # return item_exists.  Super cool to know!!

def add_order_to_db(cookie_id,quantity):
    print("checking...")
    add_order_session = Session()
    order = Orders(cookie_id=cookie_id, order_quantity=quantity)
    add_order_session.add(order)

    add_order_session.commit()
    print("order added successfully")
    add_order_session.close()
    return order

def getAllCookies():
    search_session = Session()

    all_cookies = search_session.query(Cookie).all()
    return all_cookies


def getAllOrders():
    search_session = Session()

    all_orders= search_session.query(Orders).all()
    return all_orders