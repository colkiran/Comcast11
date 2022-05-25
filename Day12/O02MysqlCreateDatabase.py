
import mysql.connector
conn = mysql.connector.connect(host = "localhost", user="root", password="",)

print(conn)

sql = "create database products"

mycursor = conn.cursor()

mycursor.execute(sql)

conn.close()
