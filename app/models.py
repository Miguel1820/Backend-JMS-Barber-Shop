from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Appointment(Base):
    __tablename__ = 'appointments'
    id = Column(Integer, primary_key=True)
    service = Column(String(100))
    client_name = Column(String(100))
    date = Column(DateTime)

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String(100))
    price = Column(Integer)

class GalleryImage(Base):
    __tablename__ = 'gallery_images'
    id = Column(Integer, primary_key=True)
    filename = Column(String(255))
    description = Column(String(200))
