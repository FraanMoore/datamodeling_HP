import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

"""class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

class Address(Base):
    __tablename__ = 'address'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person) 

    def to_dict(self):
        return {} """


class User(Base):
    __tablename__ = 'user'
    nickname = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    favorite = relationship('Favorite')

class Favorite(Base):
    __tablename__ = 'favorite'
    nickname = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    user_nickname = Column(Integer, ForeignKey('user.nickname'))
    character = relationship('Character')

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    actor = Column(String(50), nullable=False)
    house = Column(String(50), nullable=False)
    date_of_birth = Column(String(50))
    patronus = Column(String(50))
    half_blood = Column(String(50))
    favorite_nickname = Column(Integer, ForeignKey('favorite.nickname'))
    house_house = Column(Integer, ForeignKey('house.house'))

class House(Base):
    __tablename__ = 'house'
    house = Column(Integer, primary_key=True)
    character = relationship('Character')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
