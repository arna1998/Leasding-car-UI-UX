from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from be.Setting import Setting

conn=Setting().GetConn()
engine=create_engine(conn)
Sessions=sessionmaker(bind=engine)
session=Sessions()

#CRUD
class Repository_Car():
    #اضافه کردن داده
    def Add(self,obj):
        session.add(obj)
        session.commit()
        return True

    #خواندن داده ها
    def Read(self,TableName):
        return session.query(TableName).all()
        #output->List

    #خواندن یک داده
    def ReadByIdCar(self,TableName,id):
        return session.query(TableName).filter(TableName.car_id==id).first()
        #output->Object

    #حذف داده
    def Delete(self,obj):
        session.delete(obj)
        session.commit()
        return True

    #اپدیت پویا

    def UpdateCar(self,objold,objnew):
        objold.car_in=objnew.car_in
        objold.car_out=objnew.car_out
        objold.car_date=objnew.car_date
        session.commit()
        return True

    def UpdateDynamic(self,oldobj,**kwargs):
        for key,val in kwargs.items():
            setattr(oldobj,key,val)
            session.commit()
            return True
    #دو روش جستجو
    def Search(self,TableName,search):
        result = session.query(TableName).filter((TableName.car_id.like(f"%{search}%")) |
                                                 (TableName.car_in.like(f"%{search}%")) |
                                                 (TableName.car_out.like(f"%{search}%")) |
                                                 (TableName.car_date.like(f"%{search}%")))



        return result

    #چک کردن عدم ثبت فرد تکراری
    def Exist(self,TableName,newobj):
        result=session.query(TableName).filter((TableName.car_in==newobj.car_in) &
                                               (TableName.car_out==newobj.car_out)).all()
        if result==[]:
            return True
        else:
            return False

    #لاگین و ورود با رمز
    def ExistLogin(self,TableName,newobj):
        result=session.query(TableName).filter((TableName.username==newobj.username) &
                                               (TableName.password==newobj.password)).all()

        if result==[]:
            return False
        else:
            return True

