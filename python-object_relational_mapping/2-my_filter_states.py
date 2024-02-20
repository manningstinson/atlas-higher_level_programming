#!/usr/bin/python3
"""Filter states by user input.

This script connects to a MySQL server running on localhost at port 3306
and displays all values in the states table
of hbtn_0e_0_usa where name matches the provided argument.

"""

import MySQLdb
import sys


def filter_states(username, password, database, state_name):
    """Filter states by user input and display the results.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.
        state_name (str): Name of the state to search for.

    Returns:
        None
    """
    try:
        # Connect to MySQL server
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )
        # Create cursor object
        cursor = db.cursor()

        # Prepare SQL query
        # Prepare SQL query
        query = (
            "SELECT * "
            "FROM states "
            "WHERE BINARY name = %s "
            "ORDER BY id ASC"
            )

        # Execute the query
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)


if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 5:
        print("Usage: ./2-my_filter_states.py "
              "<mysql_username> "
              "<mysql_password> "
              "<database_name> "
              "<state_name_searched>")
        sys.exit(1)

    # Retrieve command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function to filter states
    filter_states(username, password, database, state_name)
