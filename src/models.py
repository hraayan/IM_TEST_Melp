
from sqlalchemy import Column,Integer, String, Float
from config import Base



class Restaurant(Base):
    __tablename__ = 'restaurants'

    id = Column(String, primary_key=True, nullable=False)
    rating = Column(Integer, nullable=False)
    name = Column(String, nullable=False)
    site = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    street = Column(String, nullable=False)
    city = Column(String, nullable=False)
    state = Column(String, nullable=False)
    lat = Column(Float)
    lng = Column(Float)