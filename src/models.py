import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

#     def to_dict(self):
#         return {}

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_id = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    favorites = Column(String(250), nullable=False)
    post_id = Column(Integer, ForeignKey('post.id'))
    post = relationship('Post')

class Planets(Base):
    __tablename__ = 'Planets'
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(250), nullable=False)
    population = Column(Integer, nullable=False)
    climate = Column(String(250), nullable=False)
    surface_water = Column(Integer, nullable=False)
    species_id = Column(Integer, ForeignKey('species.id'))
    species = relationship('Species')

class Species(Base):
    __tablename__ = 'Species'
    id = Column(Integer, primary_key=True)
    species_name = Column(String(250), nullable=False)
    language = Column(String(250), nullable=False)
    lifespan = Column(Integer, nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship('Planet')

class Vehicles(Base):
    __tablename__ = 'Vehicles'
    id = Column(Integer, primary_key=True)
    vehicle_name = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    classification = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)


## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')