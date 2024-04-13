#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON state.id=cities.states_id
        WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))
    result = cursor.fetchall()
    tmp = list(row[0] for row in result)
    print(*tmp, sep=", ")
    cursor.close()
    db.close()
