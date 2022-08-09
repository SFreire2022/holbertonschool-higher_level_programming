#!/usr/bin/python3
"""
Python script that Change the name of the State where id = 2 to New Mexico
the database hbtn_0e_6_usa, using sqlalchemy.
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
    session = Session()
    state = session.query(State).filter(State.id == 2)
    state.update({"name": ("New Mexico")})
    session.commit()
    session.close()
