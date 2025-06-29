#!/usr/bin/env python3
"""a Scrpit to connect to MySQLdb and writes to it"""
import MySQLdb
import sys

def main():
    """taking username, password and database as arguments"""
    mysql_user = sys.argv[1]
    mysql_pass = sys.argv[2]
    db_name = sys.argv[3]

    """setting up the db connection"""
    db = MySQLdb.connect(
        host = 'localhost',
        port = 3306,
        user = mysql_user,
        passwd = mysql_pass,
        db = db_name
    )
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    """fetching the query result"""

    for record in cursor.fetchall():
        print(record)
    cursor.close()
    db.close()

if __name__ == "__main__":
    main() 



