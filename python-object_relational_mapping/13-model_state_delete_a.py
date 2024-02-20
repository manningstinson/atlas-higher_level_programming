#!/usr/bin/python3
"""
Script that deletes all State objects
with a name containing the letter a
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states(username, password, db_name):
    """
    Deletes all State objects with
    a name containing the letter a
    from the specified database.
    """
    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query states with names containing the letter a and delete them
    states_to_delete = session.query(State)\
        .filter(State.name.like('%a%'))\
        .all()

    for state in states_to_delete:
        session.delete(state)

    # Commit the transaction
    session.commit()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} username password database_name".format(sys.argv[0]))
        sys.exit(1)

    # Call the function with provided arguments
    delete_states(sys.argv[1], sys.argv[2], sys.argv[3])
