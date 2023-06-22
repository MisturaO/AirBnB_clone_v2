#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship
from models import review
from models import file_storage


class Place(BaseModel, Base):
    """This class defines the table 'places' by various
    attributes(columns) for the database storage"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship("Review", cascade='all, delete-orphan',
                           backref="place")

    @property
    def reviews(self):
        """Returns the reviews associated with Place"""
        reviews_in_place = []
        for value in storage.all(Review).values():
            if value.place_id == self.id:
                reviews_in_place.append(value)
        return reviews_in_place
