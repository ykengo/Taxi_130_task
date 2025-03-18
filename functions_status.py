from sqlalchemy.orm import sessionmaker

from models import *

DATABASE_URL = "postgresql+psycopg2://school:School1234*@79.174.88.238:15221/school_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def create_status(name : str):
    db = SessionLocal()
    try:
        status = Status(status = name)
        db.add(status)
        db.commit()
        db.refresh(status)
        print("Successfuly")
        return status
    finally:
        db.close()

def update_status(status_id : int, name: str = None):
    db = SessionLocal()
    try:
        status = db.query(Status).filter(Status.id == status_id).first()
        if status:
            if name:
                status.passenger = name
            db.commit()
            db.refresh(status)
        return status
    finally:
        db.close()


def delete_status(status_id : int):
    db = SessionLocal()
    try:
        status = db.query(Status).filter(Status.id == status_id).first()
        if status:
            db.delete(status)
            db.commit()
            return True
    finally:
        db.close()

def get_status(id : int = None, name : str = None):
    db = SessionLocal()
    status = db.query(Status)
    if id:
        status.filter(Status.id == id)
    if name:
        status.filet(Status.status == name)
    try:
        return status.all()
    finally:
        db.close()

def get_all_statuses():
    db = SessionLocal()
    all_statuses = db.query(Status).all()
    return all_statuses
