# program begins here
import mysql.connector as mc # importing requied modules
mydb=mc.connect(host='localhost', user='root', password='Jesusabhi@0399') # connecting to server
mycursor=mydb.cursor() #cursor creation
#mycursor.execute("CREATE DATABASE db01")  # creating database named as db01
if mydb.is_connected():   
	print("Connection established")
else:  										#checking the connection weither connected or not
	print("Failed to connect to database")

# program ends here