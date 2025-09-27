from sqlalchemy import create_engine,Column,Integer,String,NVARCHAR,DATETIME
from sqlalchemy.orm import declarative_base
from be.Setting import Setting
import pyodbc

conn=Setting().GetConn()
engine=create_engine(str(conn))
Base=declarative_base()


class Car(Base):
    __tablename__= "Car"
    car_id=Column(Integer,primary_key=True,autoincrement=True)
    car_in=Column(NVARCHAR)
    car_out=Column(NVARCHAR)
    car_date=Column(NVARCHAR)

    def __init__(self,car_in,car_out,car_date):
        self.car_in=car_in
        self.car_out=car_out
        self.car_date=car_date

class Login(Base):
    __tablename__ = "Login"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(NVARCHAR)
    password = Column(NVARCHAR)

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.is_valid = (
        self.validate())

    def validate(self):
            # منطق اعتبارسنجی
            return self.username == "your_expected_username" and self.password == "your_expected_password"


    def __init__(self,UserName,Password):
        self.username=UserName
        self.password=Password


Base.metadata.create_all(engine)
