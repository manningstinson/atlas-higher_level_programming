#!/usr/bin/python3
"""
Script that takes in arguments
and displays all values in the states table of
hbtn_0e_0_usa where name matches the argument.
Safe from MySQL injections.

Usage:
    ./3-my_safe_filter_states.py
    <mysql username> <mysql password>
    <database name> <state name searched>

Arguments:
    mysql username: MySQL username.
    mysql password: MySQL password.
    database name: Name of the database.
    state name searched: Name of the state to search for.

Requirements:
    - Module MySQLdb (import MySQLdb).
    - Script should connect to a MySQL server
    - running on localhost at port 3306.
    - Results must be sorted in ascending order by states.id.
    - Results must be displayed as they are in the example below.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments are provided
    if len(sys.argv) != 5:
        print(
            "Usage: ./3-my_safe_filter_states.py <mysql username> "
            "<mysql password> <database name> <state name searched>"
            )

        sys.exit(1)

    # Retrieving command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # Construct the query with placeholders to prevent SQL injection
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"

    # Execute the SQL command safely
    cursor.execute(query, (state_name,))

    # Fetch all the rows in a list of tuples
    results = cursor.fetchall()

    # Print the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
