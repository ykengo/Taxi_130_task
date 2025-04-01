from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Driver, Order, Passenger, Status

app = FastAPI(title="Taxi API", description="API for managing taxi service")

DATABASE_URL = "postgresql+psycopg2://school:School1234*@79.174.88.238:15221/school_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)


class DriverBase(BaseModel):
    car_sign: str
    driver: str

    class Config:
        orm_mode = True


class DriverCreate(DriverBase):
    pass


class DriverResponse(DriverBase):
    id: int


class PassengerBase(BaseModel):
    name: str
    phone: str

    class Config:
        orm_mode = True


class PassengerCreate(PassengerBase):
    pass


class PassengerResponse(PassengerBase):
    id: int


class OrderBase(BaseModel):
    passenger_id: int
    driver_id: int
    status_id: int
    address_from: str
    address_to: str
    price: float

    class Config:
        orm_mode = True


class OrderCreate(OrderBase):
    pass


class OrderResponse(OrderBase):
    id: int


class StatusBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class StatusCreate(StatusBase):
    pass


class StatusResponse(StatusBase):
    id: int


# Driver endpoints
@app.post("/drivers/", response_model=DriverResponse)
async def create_driver_api(driver: DriverCreate):
    db = SessionLocal()
    try:
        db_driver = Driver(car_sign=driver.car_sign, driver=driver.driver)
        db.add(db_driver)
        db.commit()
        db.refresh(db_driver)
        return db_driver
    finally:
        db.close()


@app.get("/drivers/", response_model=List[DriverResponse])
async def get_drivers(
    id: Optional[int] = None, car_sign: Optional[str] = None, name: Optional[str] = None
):
    db = SessionLocal()
    try:
        query = db.query(Driver)
        if id:
            query = query.filter(Driver.id == id)
        if car_sign:
            query = query.filter(Driver.car_sign == car_sign)
        if name:
            query = query.filter(Driver.driver == name)
        return query.all()
    finally:
        db.close()


# Passenger endpoints
@app.post("/passengers/", response_model=PassengerResponse)
async def create_passenger_api(passenger: PassengerCreate):
    db = SessionLocal()
    try:
        db_passenger = Passenger(**passenger.dict())
        db.add(db_passenger)
        db.commit()
        db.refresh(db_passenger)
        return db_passenger
    finally:
        db.close()


@app.get("/passengers/", response_model=List[PassengerResponse])
async def get_passengers(id: Optional[int] = None, name: Optional[str] = None):
    db = SessionLocal()
    try:
        query = db.query(Passenger)
        if id:
            query = query.filter(Passenger.id == id)
        if name:
            query = query.filter(Passenger.name == name)
        return query.all()
    finally:
        db.close()


# Order endpoints
@app.post("/orders/", response_model=OrderResponse)
async def create_order_api(order: OrderCreate):
    db = SessionLocal()
    try:
        db_order = Order(**order.dict())
        db.add(db_order)
        db.commit()
        db.refresh(db_order)
        return db_order
    finally:
        db.close()


@app.get("/orders/", response_model=List[OrderResponse])
async def get_orders(
    id: Optional[int] = None,
    passenger_id: Optional[int] = None,
    driver_id: Optional[int] = None,
    status_id: Optional[int] = None,
):
    db = SessionLocal()
    try:
        query = db.query(Order)
        if id:
            query = query.filter(Order.id == id)
        if passenger_id:
            query = query.filter(Order.passenger_id == passenger_id)
        if driver_id:
            query = query.filter(Order.driver_id == driver_id)
        if status_id:
            query = query.filter(Order.status_id == status_id)
        return query.all()
    finally:
        db.close()


# Status endpoints
@app.post("/statuses/", response_model=StatusResponse)
async def create_status_api(status: StatusCreate):
    db = SessionLocal()
    try:
        db_status = Status(**status.dict())
        db.add(db_status)
        db.commit()
        db.refresh(db_status)
        return db_status
    finally:
        db.close()


@app.get("/statuses/", response_model=List[StatusResponse])
async def get_statuses(id: Optional[int] = None):
    db = SessionLocal()
    try:
        query = db.query(Status)
        if id:
            query = query.filter(Status.id == id)
        return query.all()
    finally:
        db.close()


# Delete for all models
@app.delete("/{model}/{item_id}")
async def delete_item(model: str, item_id: int):
    db = SessionLocal()
    try:
        model_map = {
            "drivers": Driver,
            "passengers": Passenger,
            "orders": Order,
            "statuses": Status,
        }

        if model not in model_map:
            raise HTTPException(status_code=400, detail="Invalid model name")

        item = db.query(model_map[model]).filter_by(id=item_id).first()
        if not item:
            raise HTTPException(status_code=404, detail=f"{model} not found")

        db.delete(item)
        db.commit()
        return {"message": f"{model} successfully deleted"}
    finally:
        db.close()


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
