import mysql.connector
# conn = mysql.connector.connect(host="localhost",database="village_data",user="root",password="sreedhar")
# cursor = conn.cursor()
# print(conn.is_connected())
# mysql = "select * from  village_worth"
# cursor.execute(mysql)
# rows = cursor.fetchall()
# for y in rows:
#     print(y)

#
# conn = mysql.connector.connect(host="localhost",database="village_data",user="root",password="sreedhar")
# cursor = conn.cursor()
# print(conn.is_connected())
# mysql = "select * from village_worth where si_no=3"
# cursor.execute(mysql)
# rows = cursor.fetchall()
# for x in rows:
#     print(x)

conn = mysql.connector.connect(host="localhost",database="village_data",user="root",password="sreedhar")
cursor =conn.cursor()
print(conn.is_connected())
mysql = "select * from village_worth where si_no=4 or family_income=1000000"
cursor.execute(mysql)
datas = cursor.fetchall()
for z in datas:
    print(z)