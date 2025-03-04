from sqlalchemy import Integer, String, Float, Column

from database import Base

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True,index=True)
    name = Column(String)
    price = Column(Float)
    is_offer = Column(String,nullable=False)