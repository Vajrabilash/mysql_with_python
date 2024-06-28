import mysql.connector as mc
mydb=mc.connect(host='localhost', user='root', password='Jesusabhi@0399')
mycursor=mydb.cursor()
#mycursor.execute("CREATE DATABASE db01")
if mydb.is_connected():
	print("Connection established")
else:
	print("Failed to connect to database")