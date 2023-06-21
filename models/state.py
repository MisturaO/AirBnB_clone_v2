#!/usr/bin/python3
""" State Module for HBNB project """
import models
import models.city as city
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import Relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = Relationship('City', back_populates='state',
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        cities = {}
        all_objs = models.storage.all(city.City)
        for key, value in all_objs.items():
            if value.state_id == self.id:
                cities[key] = value
        return cities
