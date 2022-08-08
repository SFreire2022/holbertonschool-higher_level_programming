#!/usr/bin/python3
"""
Python script that lists first State object from the database hbtn_0e_6_usa
Using sqlalchemy
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    try:
        states = Session().query(State.id, State.name).first()
        print("{}: {}".format(states.id, states.name))
    except Exception:
        print("Nothing")
    Session().close()
