from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship

from database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    drums = relationship("Drum", backref="owner")


class Drum(Base):
    __tablename__ = "drums"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

class Pokemon(Base):
    __tablename__ = "pokemons"

    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    name=Column(String(255))
    classification=Column(String(255))
    type1=Column(String(255))
    type2=Column(String(255))
    generation=Column(Integer)
    is_legendary=Column(Integer)
    stats=relationship("PokemonStats", backref="Pokemon", uselist=False)
    

class PokemonStats(Base):
    __tablename__ = "pokemon_stats"

    id=Column(Integer, primary_key=True, index=True, autoincrement=True)
    pokemon_id=Column(Integer, ForeignKey("pokemons.id"))
    height_m=Column(Float, nullable=True)
    weight_kg=Column(Float, nullable=True)
    attack=Column(Integer, nullable=True)

