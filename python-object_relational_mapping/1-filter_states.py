#!/usr/bin/python3

"""
1. Filter states
"""
import MySQLdb
import sys

if __name__ == "__main__":
    # connect using exactly sys.argv[1], [2], [3]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cursor = db.cursor()
    # they expect this exact query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cursor.fetchall():
        """fetchall gets the results in a tuple(number, state)
        we should focus on the stats index...that is tuple[1]
        """
        state_name = state[1]
        if state_name.startswith("N"):
            print(state)
    cursor.close()
    db.close()
