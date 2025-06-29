#!/usr/bin/python3
"""
5. All cities by state
Lists all cities of a given state (safe from SQL injection)
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Get credentials and target state from arguments
    user, passwd, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
    cursor = db.cursor()

    # Parameterized query (SQL injection safe)
    cursor.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Extract city names only, join with commas
    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    db.close()
