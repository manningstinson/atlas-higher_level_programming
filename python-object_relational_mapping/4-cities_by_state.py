#!/usr/bin/python3
"""
Script to list all cities from the database hbtn_0e_4_usa.

This script takes 3 arguments:
mysql username
mysql password
and database name.

It connects to a MySQL server
running on localhost at port 3306.

Results are sorted in ascending order by cities.id.
It uses MySQLdb module to interact with MySQL database.

Example:
    $ ./4-cities_by_state.py root root hbtn_0e_4_usa
    (1, 'San Francisco', 'California')
    (2, 'San Jose', 'California')
    (3, 'Los Angeles', 'California')
    (4, 'Fremont', 'California')
    (5, 'Livermore', 'California')
    (6, 'Page', 'Arizona')
    (7, 'Phoenix', 'Arizona')
    (8, 'Dallas', 'Texas')
    (9, 'Houston', 'Texas')
    (10, 'Austin', 'Texas')
    (11, 'New York', 'New York')
    (12, 'Las Vegas', 'Nevada')
    (13, 'Reno', 'Nevada')
    (14, 'Henderson', 'Nevada')
    (15, 'Carson City', 'Nevada')
"""

import MySQLdb
import sys


def list_cities_by_state(username, password, database):
    """List all cities by state from the database."""
    # Connect to the database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object
    cursor = db.cursor()
    # Execute the SQL query
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)
    # Fetch all the rows
    rows = cursor.fetchall()
    # Print the rows
    for row in rows:
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)
    username, password, database = sys.argv[1:]
    list_cities_by_state(username, password, database)
