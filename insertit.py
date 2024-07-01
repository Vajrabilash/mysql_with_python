import mysql.connector as mc
myconn = mc.connect(host='localhost',user='root',password='Jesusabhi@0399',database='db01')
mycursor=myconn.cursor()
# sql="INSERT INTO tba(Name,Age) VALUES (%s,%d)"
# val=('abhi',25)
mycursor.execute("INSERT INTO tba(Name,Age) VALUES('Deepu',22)");
myconn.commit();