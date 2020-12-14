#!/usr/bin/python3
"""script that that deletes all State objects with a name containing the
letter a from the database hbtn_0e_6_usa
the script takes 3 arguments: mysql username, mysql password and database name.
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from sqlalchemy import delete

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],
                                   sys.argv[2],
                                   sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like('%a%'))\
        .delete(synchronize_session=False)
    session.commit()
