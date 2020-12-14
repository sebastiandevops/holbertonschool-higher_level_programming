#!/usr/bin/python3
"""script that that changes the name of a State object from the
database hbtn_0e_6_usa.
the script takes 3 arguments: mysql username, mysql password and database name.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
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
    to_change = session.query(State)
    to_change = to_change.filter(State.id == 2)
    records = to_change.one()
    records.name = "New Mexico"
    session.commit()
