#!/usr/bin/python3
"""script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa
the script takes 4 arguments: mysql username, mysql password, database name
and state name to search
"""
import sys
from model_state import Base, State
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
    toSearch = sys.argv[4]
    result = session.query(State).filter(State.name == toSearch)\
        .order_by(State.id).first()
    if result is None:
        print("Not found")
    else:
        for state in session.query(State).filter(State.name == toSearch)\
                .order_by(State.id):
            print('{}'.format(state.id))
