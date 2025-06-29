#!/usr/bin/env python3
"""
2. Filter states by user input
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # no arg checking needed per spec
    user, pw, db_name, state_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=pw,
        db=db_name
    )
    cursor = db.cursor()

    # exact SQL pattern with format for the 4th arg
    query = (
        "SELECT * FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)
    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
