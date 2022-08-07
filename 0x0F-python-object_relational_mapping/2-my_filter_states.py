#!/usr/bin/python3
"""
Python script that takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
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
    sql_query = "SELECT * FROM states WHERE name = '{}'\
                ORDER BY states.id ASC".format(state_arg)
    cursor.execute(sql_query)
    res_query_rows = cursor.fetchall()

    for row in res_query_rows:
        if row[1] == state_arg:
            print(row)
    cursor.close()
    db.close()
