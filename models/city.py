#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.orm import declarative_base, relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    state = relationship('State', back_populates='cities')
    places = relationship('Place', back_populates='cities', cascade="all, delete-orphan")
