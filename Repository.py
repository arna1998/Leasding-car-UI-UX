from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from be.Setting import Setting

conn=Setting().GetConn()
engine=create_engine(conn)
Sessions=sessionmaker(bind=engine)
session=Sessions()

#CRUD
class Repository_Personal():
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
    def ReadByIdPersonal(self,TableName,id):
        return session.query(TableName).filter(TableName.prs_id== id).first()

        #output->Object

    #حذف داده
    def Delete(self,obj):
        session.delete(obj)
        session.commit()
        return True

    #اپدیت
    def UpdatePersonal(self,objold,objnew):
        objold.prs_person=objnew.prs_person
        objold.prs_number=objnew.prs_number
        objold.prs_date=objnew.prs_date
        session.commit()
        return True
    #اپدیت پویا


    def UpdateDynamic(self,oldobj,**kwargs):
        for key,val in kwargs.items():
            setattr(oldobj,key,val)
            session.commit()
            return True
    #دو روش جستجو
    def Search(self,TableName,search):
        result = session.query(TableName).filter((TableName.prs_id.like(f"%{search}%")) |
                                                 (TableName.prs_person.like(f"%{search}%")) |
                                                 (TableName.prs_number.like(f"%{search}%")) |
                                                 (TableName.prs_date.like(f"%{search}%")))

        return result

    #چک کردن عدم ثبت فرد تکراری
    def Exist(self,TableName,newobj):
        result=session.query(TableName).filter((TableName.prs_person==newobj.prs_person) &
                                               (TableName.prs_number==newobj.prs_number)).all()
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

