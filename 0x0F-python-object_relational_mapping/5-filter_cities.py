#!/usr/bin/python3
"""script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa
script takes 4 arguments: mysql username, mysql password, database name
and state name (SQL injection free!).
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
    string = sys.argv[4]
    c.execute("""SELECT cities.id, cities.name, states.name
               FROM cities\
               LEFT JOIN states\
               ON cities.state_id = states.id\
               WHERE states.name = %s\
               ORDER BY cities.id ASC""", (string,))
    tables = c.fetchall()
    my_list = []
    for idx, city, state in tables:
        my_list.append(city)
    join = ', '.join(my_list)
    print(join)
    c.close()
    db.close()
