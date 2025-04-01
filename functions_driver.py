from sqlalchemy.orm import sessionmaker

from models import *

DATABASE_URL = "postgresql+psycopg2://school:School1234*@79.174.88.238:15221/school_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def create_driver(sign: str, name: str):
    db = SessionLocal()
    try:
        driver = Driver(car_sign=sign, driver=name)
        db.add(driver)
        db.commit()
        db.refresh(driver)
        print("Successfuly")
        return driver
    finally:
        db.close()


def update_driver(driver_id: int, car_sign: str = None, name: str = None):
    db = SessionLocal()
    try:
        driver = db.query(Driver).filter(Driver.id == driver_id).first()
        if driver:
            if name:
                driver.driver = name
            if car_sign:
                driver.car_sign = car_sign
            db.commit()
            db.refresh(driver)
        print("Successfuly")
        return driver
    finally:
        db.close()


def delete_driver(driver_id: int):
    db = SessionLocal()
    try:
        driver = db.query(Driver).filter(Driver.id == driver_id).first()
        if driver:
            db.delete(driver)
            db.commit()
            print("Successfuly")
            return True
    finally:
        db.close()


def get_driver(id: int = None, car_sign: str = None, name: str = None):
    db = SessionLocal()
    driver = db.query(Driver)
    if id:
        driver.filter(Driver.id == id)
    if car_sign:
        driver.filter(Driver.car_sign == car_sign)
    if name:
        driver.filter(Driver.name == name)
    try:
        return driver.all()
    finally:
        db.close()


def get_all_drivers():
    db = SessionLocal()
    all_drivers = db.query(Driver).all()
    return all_drivers
