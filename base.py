#this file creates engine and base
#engine = core interface to the db (url path, echo=false????)
#Base = declarative_base() all of the maopped classes inhereit from this
#from Jennifer Plemel

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

#Engine represents the core interface to the database
#The first argument is the url of the database

engine = create_engine('sqlite:///cookie_seller.db', echo = False)

Base = declarative_base() #All of the mapped classes inherit from this