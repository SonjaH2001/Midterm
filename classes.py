from sqlalchemy import Column, Integer, String, ForeignKey
from base import Base

class Orders (Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key = True)
    cookie_id = Column(Integer, ForeignKey('cookie.id'))
    customer_id = Column(Integer, ForeignKey('customer.id'))
    order_quantity = Column(Integer)
    #need a total sale, somewhere
    # def__repr__(self)

class Cookie (Base):
    __tablename__ = 'cookie'
    id = Column(Integer, primary_key=True)
    description = Column(String)
    price = Column(Integer)

class Customer (Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)