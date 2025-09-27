from dal.Repositoryc import Repository_Car


class blCar():
    def blAdd(self,obj):
        repos=Repository_Car()
        result=repos.Add(obj)
        return result



    def blRead(self,TableName):
        repos=Repository_Car()
        result=repos.Read(TableName)
        return result

    def blReadById(self,TableName,id):
        repos=Repository_Car()
        result=repos.ReadByIdCar(TableName,id)
        return result

    def blDelete(self,TableName,id):
        repos=Repository_Car()
        objc=repos.ReadByIdCar(TableName,id)
        return repos.Delete(objc)


    def blUpdateCar(self, TableName,id,datanew):
        repos=Repository_Car()
        objc=repos.ReadByIdCar(TableName,id)
        return repos.UpdateCar(objc,datanew)

    def blUpdateDynamic(self,TableName,id,**kwargs):
        repos=Repository_Car()
        objc=repos.ReadByIdCar(TableName,id)
        return repos.UpdateDynamic(objc,**kwargs)

    def blSearch(self,TableName,search):
        repos=Repository_Car()
        lstobj=repos.Search(TableName,search)
        return lstobj

    def blExist_Car(self,TableName,newobj):
        repos=Repository_Car()
        result=repos.Exist(TableName,newobj)
        return result

    """def blExistLogin(self,TableName,newobj):
        repos=Repository_Car()
        result=repos.ExistLogin(TableName,newobj)
        return result"""

