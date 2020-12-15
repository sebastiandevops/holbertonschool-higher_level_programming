#!/usr/bin/python3
"""Class City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import relationship


Base = declarative_base()


class City(Base):
    """City class:

    inherits from Base (imported from model_state)
    links to the MySQL table cities

    class attributes:
        id: represents a column of an auto-generated,
        unique integer, can’t be null and is a primary key.
        name: represents a column of a string of 128
        characters and can’t be null.
        state_id: represents a column of an integer,
        can’t be null and is a foreign key to states.id.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
