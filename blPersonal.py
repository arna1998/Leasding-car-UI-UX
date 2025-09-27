from dal.Repository import Repository_Personal


class blPersonal():
    def blAdd(self,obj):
        repos=Repository_Personal()
        result=repos.Add(obj)
        return result



    def blRead(self,TableName):
        repos=Repository_Personal()
        result=repos.Read(TableName)
        return result

    def blReadById(self,TableName,id):
        repos=Repository_Personal()
        result=repos.ReadByIdPersonal(TableName,id)
        return result

    def blDelete(self,TableName,id):
        repos=Repository_Personal()
        objp=repos.ReadByIdPersonal(TableName,id)
        return repos.Delete(objp)

    def blUpdatePersonal(self,TableName,id,datanew):
        repos=Repository_Personal()
        objp=repos.ReadByIdPersonal(TableName,id)
        return repos.UpdatePersonal(objp,datanew)



    def blUpdateDynamic(self,TableName,id,**kwargs):
        repos=Repository_Personal()
        objp=repos.ReadByIdPersonal(TableName,id)
        return repos.UpdateDynamic(objp,**kwargs)

    def blSearch(self,TableName,search):
        repos=Repository_Personal()
        lstobj=repos.Search(TableName,search)
        return lstobj

    def blExist(self,TableName,newobj):
        repos=Repository_Personal()
        result=repos.Exist(TableName,newobj)
        return result

    def blExistLogin(self,TableName,newobj):
        repos=Repository_Personal()
        result=repos.ExistLogin(TableName,newobj)
        return result

