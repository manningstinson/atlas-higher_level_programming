#!/usr/bin/python3
"""Defines the State class and
creates a Base instance for SQLAlchemy.

This module contains the definition
of a State class that represents a state
in a MySQL database.
It also creates a Base instance for
SQLAlchemy to use.

Attributes:
    Base (sqlalchemy.ext.declarative.api.Base): A declarative base for
        SQLAlchemy to use in defining ORM classes.
    State (sqlalchemy.orm.declarative.api.DeclarativeMeta): A class that
        represents a state in the database.

"""

import sys
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# Create a declarative base
Base = declarative_base()


class State(Base):
    """Represents a state in the database.

    Attributes:
        id (sqlalchemy.schema.Column): An auto-generated, unique integer
            representing the state's ID.
        name (sqlalchemy.schema.Column): A string with a maximum of 128
            characters representing the state's name.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    # Connect to the MySQL server
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
            ),
        pool_pre_ping=True
        )

    # Create all defined tables in the database
    Base.metadata.create_all(engine)
