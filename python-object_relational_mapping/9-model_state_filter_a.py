#!/usr/bin/python3
"""
9. Contains `a`
Lists all State objects that contain the letter 'a'
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine with user/pass/db from args
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states containing 'a', ordered by id
    results = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

    for state in results:
        print(f"{state.id}: {state.name}")

    session.close()
