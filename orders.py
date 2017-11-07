from sqlalchemy import Column, Interger, String

class Orders:
    __tablename__ = 'orders'
    id = Column(Integer, primary_key = True)