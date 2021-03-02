import mysql.connector
import cv2
import numpy as np

sql = '''CREATE FUNCTION nullupdate(time_)
	  IF timeIn IS NULL  THEN UPDATE attedance set timeIn = '121' where id = '001';
	  ELSEIF timeOut IS NULL THEN UPDATE attendance set timeOut = '121' where id ='001';
	ENDIF; '''

sql1 = '''select id, if(timeIn is null,'true','False'), if(timeOut is null,'true','False') from attendance where id = 002''' 


sql2 = '''select id, if(timeIn is null,insert into attendance (timeIn) values('23:00:00'),'False'), if(timeOut is null,'insert into attendance (timeIn) values('23:00:00')','False') from attendance '''

def updateNullValue():
	valueToEnter = "'12:00:00'"
	id = '002'
	conn = mysql.connector.connect(host = 'localhost',
					username = 'root',
					password = 'root',
					database='EmployeeAttendance')
	cursor = conn.cursor()
	cursor.execute(sql1)
	result = cursor.fetchall()
	#print(result)
	resulttupe = result[0]
	#print(resulttupe[1])
	if(resulttupe[1] == 'true'):
		cursor.execute('UPDATE attendance SET timeIn = '+valueToEnter+' where id = '+id)
		conn.commit()
		return
	if(resulttupe[2] == 'true'):
		cursor.execute('UPDATE attendance SET timeOut = '+valueToEnter+' where id = '+id)
		conn.commit()
		return


####   to delete entire row ####
def deleteRow(table_name,id):
	conn = mysql.connector.connect(host = 'localhost',
					username = 'root',
					password = 'root',
					database='EmployeeAttendance')
	cursor = conn.cursor()
	cursor.execute('DELETE FROM '+ table_name +' WHERE id = {0}'.format(id))
	conn.commit()
	cursor.execute("select * from attendance")
	result = cursor.fetchall()
	print(result);

#### to delete a perticular column value in a row ####
def deleteColumnValue(table_name,columname,id):
	conn = mysql.connector.connect(host = 'localhost',
					username = 'root',
					password = 'root',
					database='EmployeeAttendance')
	cursor = conn.cursor()
	cursor.execute('UPDATE '+ table_name +' SET '+columname+ ' = NULL '+' where id = '+id)	
	cursor.execute("select * from attendance")
	result = cursor.fetchall()
	print(result);


### update value to existing row ###
def updateValuecolumn(table_name,columname,valueToEnter,id):
	conn = mysql.connector.connect(host = 'localhost',
					username = 'root',
					password = 'root',
					database='EmployeeAttendance')
	cursor = conn.cursor()
	cursor.execute('UPDATE '+ table_name +' SET '+columname+ ' = '+valueToEnter+' where id = '+id)
	conn.commit()
	cursor.execute("select * from attendance")
	result = cursor.fetchall()
	print(result);

def insertValuesTOTable():
	conn = mysql.connector.connect(host = 'localhost',
						username = 'root',
						password = 'root',
						database='EmployeeAttendance')
	cursor = conn.cursor()
	cursor.execute(countQuery)	#finding the number of columns
	columns = cursor.fetchall()	# return value like [(count of columns,)]
	tupleV = columns[0]		# make into tuple = (count of columns,)
	print(type(tupleV[0]))	

		


	
def insertValues():
	conn = mysql.connector.connect(host = 'localhost',
					username = 'root',
					password = 'root',
					database='EmployeeAttendance')
	cursor = conn.cursor()
	cursor.execute(countQuery)	#finding the number of columns
	columns = cursor.fetchall()	# return value like [(count of columns,)]
	tupleV = columns[0]		# make into tuple = (count of columns,)
	print(type(tupleV[0]))		#get int value '''count''' 
	
	insertValues = []
	values = ''
	c = 0	
	while(c<2):
		for i in range(0,tupleV[0]):
			string = input("enter"+str(i+1)+" row values")
			values = values+string
		
		tupleFormat = tuple(map(str,values))	# entered value is in tupe format
		values = ''
		insertValues.append(tupleFormat)
		del tupleFormat
		c = c+1	
	print(insertValues)

updateNullValue()
#deleteRow('attendance','001')
#deleteColumnValue('attendance','timeInt','001')	
#updateValuecolumn('attendance','timeIn',"'11:30:56'",'001')
#insertValues()





