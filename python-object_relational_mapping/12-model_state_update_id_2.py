#!/usr/bin/python3
"""
Script that changes the name of a State object in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    """Main function to update the state name."""
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        return

    # Arguments for MySQL connection
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Create engine to connect to MySQL server
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database))

    # Create a configured 'Session' class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Update the state name where id = 2 to "New Mexico"
    state_to_update = session.query(State).filter_by(id=2).first()
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    main()
