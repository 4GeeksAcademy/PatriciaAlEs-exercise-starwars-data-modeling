import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    email = Column(String(30), nullable=False, unique=True)
    username = Column(String(30), nullable=False, unique=True)
    firstname = Column(String(30), nullable=False)               
    last_name = Column(String(30), nullable=False)
    email = Column(String(50), nullable=False)
    password = Column(String(30), nullable=False)
    favoritos = relationship('Favoritos', back_populates='user')


class Favoritos(Base):
    __tablename__ = 'Favoritos'
    id = Column(Integer, primary_key=True)
    planeta_id = Column(Integer, ForeignKey('Planeta.id'), nullable=False)
    personaje_id = Column(Integer, ForeignKey('Personaje.id'), nullable=False)
    vehiculo_id = Column(Integer, ForeignKey('Vehiculo.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    user = relationship('User', back_populates='favoritos')
    # para las relaciones uno a muchos con las otras tablas (planetas, vehiculos, personajes)
    planeta_id = Column(Integer, ForeignKey('Planetas.id'), nullable=True)
    personaje_id = Column(Integer, ForeignKey('Personajes.id'), nullable=True)
    vehiculo_id = Column(Integer, ForeignKey('Vehiculos.id'), nullable=True)
    # Relaciones con las otras tablas
    planeta = relationship('Planetas')
    personaje = relationship('Personajes')
    vehiculo = relationship('Vehiculos')


class Planetas(Base):
    __tablename__ = 'Planetas'
    id = Column(Integer, primary_key=True)
    nombre_planeta = Column(String(250), nullable=False)
    ubicacion_planeta = Column(String(250), nullable=False)
    habitantes = Column(String(250), nullable=False)

class Personajes(Base):
    __tablename__ = 'Personajes'
    id = Column(Integer, primary_key=True)
    nombre_personaje = Column(String(250), nullable=False)
    peliculas_personaje = Column(String(250), nullable=False)
    raza_personaje = Column(String(250), nullable=False)


class Vehiculos(Base):
    __tablename__ = 'Vehiculos'
    id = Column(Integer, primary_key=True)
    nombre_vehiculo = Column(String(250), nullable=False)
    peliculas_vehiculo = Column(String(250), nullable=False)
    pasajeros = Column(String(250), nullable=False)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
