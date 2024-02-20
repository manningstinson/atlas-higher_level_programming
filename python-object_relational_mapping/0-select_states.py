#!/usr/bin/python3
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
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to select states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

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
