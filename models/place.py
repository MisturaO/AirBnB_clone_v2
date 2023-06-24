#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'),
           primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'),
           primary_key=True, nullable=False)
)


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
    amenities = relationship('Amenity', secondary=place_amenity,
                             viewonly=False)

    @property
    def reviews(self):
        """Returns the reviews associated with Place"""
        reviews_in_place = []
        for value in models.storage.all(Review).values():
            if value.place_id == self.id:
                reviews_in_place.append(value)
        return reviews_in_place

    @property
    def amenities(self):
        """Returns the list of Amenity instances based on the attribute
        amenity_ids that contains all Amenity.id linked to the Place"""
        amenities_in_place = []
        for value in models.storage.all(Amenity):
            if value.place_id == self.id:
                amenities_in_place.append(value)
