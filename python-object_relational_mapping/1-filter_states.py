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
running on localhost at port 3306 with the provided username,
password, and database name, retrieves
the states with names starting with 'N', sorts them by id,
and displays them.
"""


import MySQLdb

def filter_states(username, password, database):
    """Connects to the database, filters states with names starting with "N",
    sorts results by ID, and displays them in the desired format.

    Args:
        username (str): The username for database access.
        password (str): The password for database access.
        database (str): The name of the database to connect to.
    """

    try:
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            password=password,
            database=database,
            port=3306
        )
        cursor = db.cursor()

        # Filter states with names starting with "N" and sort by ID (case-insensitive)
        query = "SELECT * FROM states WHERE name LIKE 'N%' COLLATE utf8mb4_general_ci ORDER BY id ASC"
        cursor.execute(query)

        # Fetch and display results
        for row in cursor.fetchall():
            print(row)

    except MySQLdb.Error as err:
        print("Error connecting to database:", err)

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()

if __name__ == "__main__":
    username = "root"
    password = "root"  # Replace with your actual password
    database = "test_1"  # Use the correct database name
    filter_states(username, password, database)
