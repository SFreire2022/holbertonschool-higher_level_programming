#!/usr/bin/python3
"""
Python script that takes in an argument (state) and displays all cities
in table of hbtn_0e_4_usa.
Safe from MySQL injections!
"""

from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8")
    state_arg = argv[4]
    cursor = db.cursor()
    sql_query = "SELECT cities.name FROM cities JOIN states\
                ON cities.state_id = states.id\
                WHERE states.name = %s ORDER by cities.id ASC"
    cursor.execute(sql_query, (state_arg,))
    res_query_rows = cursor.fetchall()

    print(", ".join(row[0] for row in res_query_rows))
    cursor.close()
    db.close()
