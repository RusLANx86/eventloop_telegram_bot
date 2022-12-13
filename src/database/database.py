from sqlalchemy import create_engine, Column, TEXT, INTEGER, BOOLEAN, FLOAT, DATETIME, TIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session

url_db = 'database/sqlite3.db'
engine = create_engine('sqlite:///{}'.format(url_db), connect_args={'check_same_thread': False})
session = Session(engine)

BASE = declarative_base()


class BikeRides(BASE):

    __tablename__ = "bike_rides"

    uid = Column(TEXT, primary_key=True)
    creator = Column(TEXT, nullable=False)
    ride_name = Column(TEXT, default='')
    meet_point = Column(TEXT, default='')
    ride_datetime = Column(TEXT)
    meet_time = Column(TEXT)
    description = Column(TEXT, default='')


BASE.metadata.create_all(bind=engine)
