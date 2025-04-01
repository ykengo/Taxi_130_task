from operator import truediv

from sqlalchemy.orm import sessionmaker
import datetime

from models import *
from functions_passenger import *
from functions_driver import *
from functions_status import *

DATABASE_URL = "postgresql+psycopg2://school:School1234*@79.174.88.238:15221/school_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


def create_order(adress1: str, adress2: str, driver: str, passenger: str, status: str):
    try:
        driver = int(driver)
    except ValueError:
        driver = get_driver(None, driver)[0].id
    try:
        passenger = int(passenger)
    except ValueError:
        passenger = get_passenger(passenger)[0].id
    try:
        status = int(status)
    except ValueError:
        status = get_status(status)[0].id
    current_datetime = datetime.datetime.now()
    db = SessionLocal()
    try:
        order = Order(
            adress1=adress1,
            adress2=adress2,
            date=current_datetime,
            driver=driver,
            passenger=passenger,
            status=status,
        )
        db.add(order)
        db.commit()
        db.refresh(order)
        print("Successfuly")
        return order
    finally:
        db.close()


def update_order(
    order_id: int,
    adress1: str = None,
    adress2: str = None,
    driver: str = None,
    passenger: str = None,
    status: str = None,
):
    try:
        driver = int(driver)
    except ValueError:
        driver = get_driver(None, driver)[0].id
    try:
        passenger = int(passenger)
    except ValueError:
        passenger = get_passenger(passenger)[0].id
    try:
        status = int(status)
    except ValueError:
        status = get_status(status)[0].id
    db = SessionLocal()
    try:
        order = db.query(Order).filter(Order.id == order_id).first()
        if order:
            if adress1:
                order.adress1 = adress1
            if adress2:
                order.adress2 = adress2
            if driver:
                order.driver = driver
            if passenger:
                order.passenger = passenger
            if status:
                order.status = status
            db.commit()
            db.refresh(order)
        return order
    finally:
        db.close()


def delete_order(order_id: int):
    db = SessionLocal()
    try:
        order = db.query(Order).filter(Order.id == order_id).first()
        if order:
            db.delete(order)
            db.commit()
            return True
    finally:
        db.close()


def get_all_orders():
    db = SessionLocal()
    all_orders = db.query(Order).all()
    return all_orders


def get_order(
    adress1: str = None,
    adress2: str = None,
    driver: str = None,
    passenger: str = None,
    status: str = None,
):
    db = SessionLocal()
    try:
        driver = int(driver)
    except ValueError:
        driver = get_driver(None, driver)[0].id
    try:
        passenger = int(passenger)
    except ValueError:
        passenger = get_passenger(passenger)[0].id
    try:
        status = int(status)
    except ValueError:
        status = get_status(status)[0].id
    order = db.query(Order)
    if adress1:
        order.filter(Order.adress1 == adress1)
    if adress2:
        order.filter(Order.adress2 == adress2)
    if driver:
        order.filter(Order.driver == driver)
    if passenger:
        order.filter(Order.passenger == passenger)
    if status:
        order.filter(Order.status == status)
    try:
        return order.all()
    finally:
        db.close()
