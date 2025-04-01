from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Date,
    ForeignKey,
    MetaData,
    text,
)
import psycopg2
from sqlalchemy.orm import relationship, declarative_base

metadata = MetaData(schema="kazancev_yakovlev")
Base = declarative_base(metadata=metadata)

DATABASE_URL = "postgresql+psycopg2://school:School1234*@79.174.88.238:15221/school_db"


class Order(Base):
    __tablename__ = "orders"
    __table_args__ = {"schema": "kazancev_yakovlev"}

    id = Column(Integer, primary_key=True)
    adress1 = Column(String)
    adress2 = Column(String)
    date = Column(Date)
    driver = Column(Integer, ForeignKey("kazancev_yakovlev.drivers.id"))
    passenger = Column(Integer, ForeignKey("kazancev_yakovlev.passengers.id"))
    status = Column(Integer, ForeignKey("kazancev_yakovlev.statuses.id"))

    driver_rel = relationship("Driver", back_populates="orders")
    passenger_rel = relationship("Passenger", back_populates="orders")
    status_rel = relationship("Status", back_populates="orders")

    def __repr__(self):
        return f"<Order(id = '{self.id}', from = '{self.adress1}', to = '{self.adress2}', date = '{self.date}', driver_id = '{self.driver_rel}', passenger_id = '{self.passenger_rel}', status_id = '{self.status_rel}')>"


class Driver(Base):
    __tablename__ = "drivers"
    __table_args__ = {"schema": "kazancev_yakovlev"}

    id = Column(Integer, primary_key=True)
    car_sign = Column(String)
    driver = Column(String)

    orders = relationship("Order", back_populates="driver_rel")

    def __repr__(self):
        return f"<Driver(id = '{self.id}', car sign = '{self.car_sign}', name = '{self.driver}')>"


class Passenger(Base):
    __tablename__ = "passengers"
    __table_args__ = {"schema": "kazancev_yakovlev"}

    id = Column(Integer, primary_key=True)
    passenger = Column(String)

    orders = relationship("Order", back_populates="passenger_rel")

    def __repr__(self):
        return f"<Passenger(id = '{self.id}', passenger='{self.passenger}')>"


class Status(Base):
    __tablename__ = "statuses"
    __table_args__ = {"schema": "kazancev_yakovlev"}

    id = Column(Integer, primary_key=True)
    status = Column(String)

    orders = relationship("Order", back_populates="status_rel")

    def __repr__(self):
        return f"<Status(id = '{self.id}', name ='{self.status}')>"


def create_tables(engine):
    Base.metadata.create_all(engine)


if __name__ == "__main__":
    engine = create_engine(DATABASE_URL)
    with engine.connect() as connection:
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS kazancev_yakovlev"))
        connection.commit()
    create_tables(engine)
