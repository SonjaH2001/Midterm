# from sqlalchemy import create_engine
# from sqlalchemy import exc
# from sqlalchemy import event
# from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from base import *

# from sales import Sale
# from events import Event
from classes import Cookie
# import ui
import classes

#from Jennifer Plemel

def DB_setup():
    # Base = declarative_base() #All of the mapped classes inherit from this class
    Base.metadata.create_all(engine)  # Create a table for all the classes that use Base

    '''Need a session to talk to the database'''
    # A session manages mappings of objects to rows in the database
    # Make a session class -- only need to do this one time
    Session = sessionmaker(bind=engine)  # using the engine created earlier

    setup_session = Session()

    cookie1 = Cookie(description = 'Seasonal Sensation', price = '5')
    cookie2 = Cookie(description = 'Sugar Hill Gang', price = '5')
    cookie3 = Cookie(description = 'Chocolate Pinky Delights', price = '5')
    cookie4 = Cookie(description = 'Chocolate Chip Peanut BUtter Dream', price ='5')
    # Add cookie object to session -- this tells the session that you want to map
    # the cookie object to a row in the DB
    for item in [cookie1, cookie2, cookie3, cookie4]:
        setup_session.add(item)
    #saves when committed and closed
    setup_session.commit()
    setup_session.close()