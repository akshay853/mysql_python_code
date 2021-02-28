class sqlProperties:
    name = None
    datatype = None
    length = None
    primaryKey = False
    NotNull = False
    autoIncrement = False
    foreignKey = False

    def sqlProperties(self):
        if self.name is not None and self.datatype is not None: 
            if self.length is not None:
                if self.primaryKey is not False:
                    if self.NotNull is not False:  
                        if self.autoIncrement is not False:
                            print("name, datatype, length, primaryKey, notnull, autoIncrement")
                        else:
                            print("name, datatype, length, primaryKey, notnull")
                    elif self.autoIncrement is not False:
                        print("name, datatype, length, primaryKey,autoincrement")
                elif self.foreignKey is not False:
                    if self.NotNull is not False:
                        if self.autoIncrement is not False:
                            print("name, datatype, length,notnull, autoincrement, foreignkey ")
                        print("name, datatype, length,notnull, foreignkey ")
                    elif self.autoIncrement is not False:
                        print("name, datatype, length, autoincrement, foreignkey")   
                else:
                    if self.NotNull is not False:
                        if self.autoIncrement is not False:
                            print("name, datatype, length, notnull, autoincrement")
                        print("name, datatype, length, notnull")
                    elif self.autoIncrement is not False:
                        print("name, datatype, length, autoincrement")
            elif self.primaryKey is not False:
                    if self.NotNull is not False:  
                        if self.autoIncrement is not False:
                            print("name, datatype, primaryKey, notnull, autoIncrement")
                        else:
                            print("name, datatype, primaryKey, notnull")
                    elif self.autoIncrement is not False:
                        print("name, datatype, primaryKey,autoincrement")
            elif self.foreignKey is not False:
                if self.NotNull is not False:
                    if self.autoIncrement is not False:
                        print("name, datatype,notnull, autoincrement, foreignkey ")
                    print("name, datatype,notnull, foreignkey ")
                elif self.autoIncrement is not False:
                    print("name, datatype, autoincrement, foreignkey")   
            elif self.NotNull is not False:
                if self.autoIncrement is not False:
                    print("name, datatype, notnull, autoincrement")
                print("name, datatype, length, notnull")
            elif self.autoIncrement is not False:
                print("name, datatype, autoincrement")                     
            else:
                print("name , datatype")
        else:
            print("enter datatype and name")





class mysql(sqlProperties):
    def database_connection(self,table_name,colum12 = []):
        sql = sqlProperties()
        sql.name, sql.datatype, sql.length, sql.primaryKey, sql.NotNull, sql.autoIncrement, sql.foreignKey = colum12
        sql.sqlProperties()
    

mysql = mysql()
colum1 = ['name','int',None,True,True,False,False]
mysql.database_connection("student",colum1)