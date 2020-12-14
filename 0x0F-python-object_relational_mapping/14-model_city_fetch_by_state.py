#!/usr/bin/python3
"""script that prints all City objects from the database hbtn_0e_14_usa:
hbtn_0e_6_usa.add() and takes 3 arguments: mysql username,
mysql password and database name.
"""
import sys
from model_state import Base, State
from model_city import Base, City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State, City).order_by(cities.id).all():
        print('{}: {} {}'.format(state.name, cities.id, cities.name))
