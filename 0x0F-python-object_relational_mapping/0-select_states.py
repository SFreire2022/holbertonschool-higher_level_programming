#!/usr/bin/python3
"""
Paython script that lists all states from the database hbtn_0e_0_usa
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
    cursor = db.cursor()
    sql_query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(sql_query)
    res_query_rows = cursor.fetchall()

    for row in res_query_rows:
        print(row)
    cursor.close()
    db.close()
