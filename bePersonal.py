from sqlalchemy import create_engine,Column,Integer,String,NVARCHAR,DATETIME
from sqlalchemy.orm import declarative_base
from be.Setting import Setting
import pyodbc

conn=Setting().GetConn()
engine=create_engine(str(conn))
Base=declarative_base()

class Personal(Base):
    __tablename__="Personal"
    prs_id=Column(Integer,primary_key=True,autoincrement=True)
    prs_person=Column(NVARCHAR)
    prs_number=Column(NVARCHAR)
    prs_date=Column(NVARCHAR)

    def __init__(self,prs_person,prs_number,prs_date):
        self.prs_person=prs_person
        self.prs_number=prs_number
        self.prs_date=prs_date


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
