#!/usr/bin/python3
"""
Module to list all cities of a given state
from the hbtn_0e_4_usa database.

Usage:
    ./5-filter_cities.py
    <mysql_username>
    <mysql_password>
    <database_name>
    <state_name>

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: Name of the MySQL database
    state_name: Name of the state to filter cities

Example:
    ./5-filter_cities.py root root hbtn_0e_4_usa Texas
"""

import MySQLdb
import sys


def filter_cities(mysql_username, mysql_password, database_name, state_name):
    """Filter cities by state name and display them."""
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_password,
                         db=database_name,
                         port=3306)

    cursor = db.cursor()
    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (state_name,))
    cities = cursor.fetchall()
    db.close()

    if cities:
        cities_list = ', '.join(city[0] for city in cities)
        print(cities_list)
    else:
        print("No cities found for the given state.")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print(
            "Usage: ./5-filter_cities.py <mysql_username> <mysql_password>"
            " <database_name> <state_name>"
        )

        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_cities(
            mysql_username,
            mysql_password,
            database_name,
            state_name
        )
