from sqlalchemy.orm import sessionmaker

from models import *

DATABASE_URL = "postgresql+psycopg2://school:School1234*@79.174.88.238:15221/school_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)



def create_passenger(name : str):
    db = SessionLocal()
    try:
        psngr = Passenger(passenger = name)
        db.add(psngr)
        db.commit()
        db.refresh(psngr)
        print("Successfuly")
        return psngr
    finally:
        db.close()

def update_passenger(passenger_id : int, name: str = None):
    db = SessionLocal()
    try:
        psngr = db.query(Passenger).filter(Passenger.id == passenger_id).first()
        if psngr:
            if name:
                psngr.passenger = name
            db.commit()
            db.refresh(psngr)
        return psngr
    finally:
        db.close()


def delete_passenger(passenger_id : int):
    db = SessionLocal()
    try:
        psngr = db.query(Passenger).filter(Passenger.id == passenger_id).first()
        if psngr:
            db.delete(psngr)
            db.commit()
            return True
    finally:
        db.close()

def get_passenger(id : int = None, name : str = None):
    db = SessionLocal()
    passenger = db.query(Passenger)
    if id:
        passenger.filter(Passenger.id == id)
    if name:
        passenger.filter(Passenger.passenger == name)
    try:
        return passenger.all()
    finally:
        db.close()

def get_all_passengers():
    db = SessionLocal()
    all_psngrs = db.query(Passenger).all()
    return all_psngrs
