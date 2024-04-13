#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         passwd=mysql_password, db=db_name, port=3306)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name
                   LIKE 'N%' ORDER BY id ASC""")
    result = cursor.fetchall()
    for r in result:
        print(r)
    cursor.close()
    db.close()
