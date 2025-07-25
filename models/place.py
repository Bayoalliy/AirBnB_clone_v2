#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Float, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
import models
from os import getenv


place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60),
           ForeignKey('places.id'), primary_key=True,
           nullable=False),
    Column('amenity_id', String(60),
           ForeignKey('amenities.id'), primary_key=True,
           nullable=False)
    )


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(60))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            'Review', backref='place',
            cascade="all, delete-orphan"
            )

        amenities = relationship(
                'Amenity', secondary=place_amenity,
                viewonly=False,
                back_populates="place_amenities"
                )

    else:
        @property
        def reviews(self):
            lst = []
            for obj in models.storage.all().values():
                if type(obj) == Review and obj.place_id == self.id:
                    lst.append(obj)
            return lst

        @property
        def amenities(self):
            return self.amenity_ids

        @amenities.setter
        def amenities(self, value):
            if type(value).__name__ == 'Amenity':
                self.amenity_ids.append(value.id)
