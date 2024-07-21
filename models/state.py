#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter of cities attribut"""
        tmp = []
        for value in sorage.all().values():
            if value.__class__ == City:
                if value.state_id == self.id:
                    tmp.push(value)
        return tmp
