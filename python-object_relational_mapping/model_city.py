"""Defines the City class for ORM and database operations."""

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """City class representing cities in the database."""

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    def __repr__(self):
        """String representation of a City object."""
        return ("<City(id={}, "
                "name={}, "
                "state_id={})>").format(self.id, self.name, self.state_id)
