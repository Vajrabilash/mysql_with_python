#program begins here
import mysql.connector as mc  #importing required modules
mydb = mc.connect(host='localhost',user='root',password='Jesusabhi@0399', db='db01') #connecting to the database and server
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE tbA(Name VARCHAR(20), Age VARCHAR(15))")  #query to create table in database
#program ends here