#!/usr/bin/python3
"""Adds a new state to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state(username, password, db_name):
    """Adds a new state to the database hbtn_0e_6_usa"""
    # Create the engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name))

    # Create all tables in the engine
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Add Louisiana to the database
    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    # Print the new states.id after creation
    print(new_state.id)


if __name__ == "__main__":
    # Check if the script is called properly
    if len(sys.argv) != 4:
        print(
            "Usage: {} <username> <password> <db_name>".format(sys.argv[0])
            )
        sys.exit(1)

    # Extract arguments
    username, password, db_name = sys.argv[1:]

    # Call the function to add the state
    add_state(username, password, db_name)
