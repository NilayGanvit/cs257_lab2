# Question 4
import mysql.connector
conn_obj = mysql.connector.connect(host="localhost", user="root", passwd="12345678", database="python")
print(conn_obj) 