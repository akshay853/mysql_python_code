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
    def database_connection(self,table_name):
     
        sql = sqlProperties()
        sql.name = 'id'
        sql.datatype = 'varchar'
        #sql.length = 255
        #sql.primaryKey = True
        sql.NotNull = True
        sql.autoIncrement = True
        sql.foreignKey = True
        sql.sqlProperties()
    

mysql = mysql()
mysql.database_connection("student")