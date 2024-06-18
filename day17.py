##day17 mysql to python feb 13
import mysql.connector
conn = mysql.connector.connect(host="localhost",database="sql_data",user="root",password="sreedhar")

cursor = conn.cursor()

print(conn.is_connected())
mysql = "select * from  sql_queries where query_no=1"
cursor.execute(mysql)
rows=cursor.fetchall()
for x in rows:
    print(x)





# Import the MySQL connector module.
# Establish a connection to the MySQL database using provided credentials.
# Create a cursor object to execute SQL queries.
# Check if the connection is active and print the status.
# Define an SQL query to select all columns from sql_queries where query_no equals 1.
# Execute the SQL query using the cursor.
# Fetch all results of the query into a list of tuples.
# Iterate over the results and print each row