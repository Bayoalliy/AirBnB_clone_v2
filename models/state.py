#!/usr/bin/python3
"""
Write a class State that inherits from BaseModel:

models/state.py
Public class attributes:
name: string - empty string

Update FileStorage to manage correctly serialization and
deserialization of State.

Update your command interpreter (console.py) to allow show,
create, destroy, update and all used with State.
"""
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv

class State(BaseModel, Base):
    """inherits from BaseModel and defines the state object"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', back_populates='state', cascade="all, delete-orphan")
    else:
        from models import storage
        name = ""

        @property
        def cities(self):
            cities_lst = []
            for k, v in storage.all().items():
                if type(v) == City and v.state_id == self.id:
                    cities_lst.push(v)
            return cities_lst
