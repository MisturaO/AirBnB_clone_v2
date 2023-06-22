#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place


class City(BaseModel, Base):
    """ The city class, contains state ID and name.
        Updated to DBStorage from file storage """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    # state = Relationship('State',, back_populates='cities')

    """Relationship is created with the place table(i.e.
    the Place class model)"""
    places = relationship("Place", cascade='all, delete-orphan',
                          backref="cities")
