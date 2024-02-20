#!/usr/bin/python3
"""
Script to list all states with names
starting with 'N' from the database hbtn_0e_0_usa.

Usage:
    ./1-filter_states.py <username> <password> <database>

Arguments:
    <username>: MySQL username.
    <password>: MySQL password.
    <database>: Database name.

Example:
    ./1-filter_states.py root root hbtn_0e_0_usa

This script connects to a MySQL server
running on localhost at port 3306 with
the provided username,
password, and database name,
retrieves the states with names
starting with 'N', sorts them by id,
and displays them.
"""


import MySQLdb
import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=database
        )

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to select states starting with 'N'
        cursor.execute(
            "SELECT * FROM states WHERE "
            "name LIKE 'N%' OR "
            "name LIKE 'n%' "
            "ORDER BY id ASC"
            )

        # Fetch all the rows in a list of lists
        results = cursor.fetchall()

        # Display results
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close the database connection
        db.close()


if __name__ == "__main__":
    main()
