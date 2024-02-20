#!/usr/bin/python3
"""Fetches and prints all City objects from the database."""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def main():
    """Connects to the database and
    prints City objects by state."""
    if len(sys.argv) != 4:
        print(
            "Usage: python 14-model_city_fetch_by_state.py "
            "<username> <password> <database>"
            )

        sys.exit(1)

    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Establishing connection to the database
    engine = create_engine(
            f'mysql+mysqldb://{username}:{password}@'
            'localhost:3306/{database}'
            )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetching and printing City objects by state
    cities = session.query(City).order_by(City.id).all()
    for city in cities:
        print(f"{city.state.name}: ({city.id}) {city.name}")

    session.close()


if __name__ == "__main__":
    main()
