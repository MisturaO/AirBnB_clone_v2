#!/usr/bin/python3
"""This module defines a class User:
    Updated to DBStorage from file storage"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place


class User(BaseModel, Base):
    """This class defines the table 'users' by variouss
    attributes(columns) for the database storage"""
    __tablename__ = 'users'
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)

    """Relationship is created with the place
    table(i.e. the Place class model)"""
    places = relationship("Place", cascade='all, delete-orphan',
                          backref="user")
