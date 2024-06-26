#!/usr/bin/python3
"""Script that lists all State objects, and corresponding City objects"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import relationship
from sqlalchemy import (create_engine)


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for ins in session.query(State).order_by(State.id):
        print(ins.id, ins.name, sep=": ")
        for city_ins in ins.cities:
            print("    ", end="")
            print(city_ins.id, city_ins.name, sep=": ")
