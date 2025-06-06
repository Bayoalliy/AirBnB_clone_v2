#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Float, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import relationship
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
    if getenv("HBNB_TYPE_STORAGE") == "db":
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
        user = relationship('User', back_populates='places')
        cities = relationship('City', back_populates='places')
        reviews = relationship('Review', back_populates='place', cascade="all, delete-orphan")

        amenities = relationship(
                'Amenity', secondary=place_amenity,
                viewonly=False,
                back_populates="place_amenities"
                )

    else:
        from models import storage
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            return [obj for obj in storage.all().values() if type(obj) == Review and obj.place_id == self.id]

        @property
        def amenities(self):
            lst = []
            for val in storage.all().values():
                if type(val) == Amenity and self.id in val.amenity_ids:
                    lst.append(val)
            return lst

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)

