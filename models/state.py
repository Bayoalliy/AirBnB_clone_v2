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
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
import models


class State(BaseModel, Base):
    """inherits from BaseModel and defines the state object"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade="all, delete-orphan"
        )

    @property
    def cities(self):
        from models.city import City
        cities_lst = []
        for k, v in models.storage.all().items():
            if type(v) == City and v.state_id == self.id:
                cities_lst.append(v)
        return cities_lst
