#!/usr/bin/python3
"""
Python script that lists all State objects from the database hbtn_0e_6_usa
Using sqlalchemy
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    states = Session().query(State.id, State.name).order_by(State.id)
    for id, name in states:
        print("{:d}: {}".format(id, name))
    Session().close()
