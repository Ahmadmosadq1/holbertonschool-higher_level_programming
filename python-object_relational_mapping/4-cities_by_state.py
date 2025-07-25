#!/usr/bin/python3
"""
4. Cities by states
Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # Connect to MySQL
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()

    # One execute only: join cities with states, order by cities.id
    cursor.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    # Print results exactly as requested
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
