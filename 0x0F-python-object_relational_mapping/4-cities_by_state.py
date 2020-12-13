#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
script takes 3 arguments: mysql username, mysql password and database name
The script connects to MySQL server running on localhost at port 3306.
Results must be sorted in ascending order by states.id
Results must be displayed as they are in the example below
The code should not be executed when imported.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("""SELECT cities.id, cities.name, states.name
               FROM cities\
               LEFT JOIN states\
               ON cities.state_id = states.id\
               ORDER BY cities.id ASC""")
    tables = c.fetchall()
    for items in tables:
        print(items)
    c.close()
    db.close()
