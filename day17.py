##day17 mysql to python feb 13
import mysql.connector
conn = mysql.connector.connect(host="localhost",database="sql_data",user="root",password="sreedhar")

cursor = conn.cursor()

print(conn.is_connected())
mysql= "select * from  sql_queries where id=1"
cursor.execute(mysql)
rows=cursor.fetchall()
for x in rows:
    print(x)
