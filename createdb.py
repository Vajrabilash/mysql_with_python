import mysql.connector as mc   # importing required modules 
mydb = mc.connect(host='localhost', user='root', password='Jesusabhi@0399')  #connecting database
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE db02")     #query to create database

mycursor.execute("SHOW DATABASES") 			#query to show databases
				
for x in mycursor:
	print(x)			#printing the databases using for loops