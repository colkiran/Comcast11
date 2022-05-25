
import mysql.connector

conn = mysql.connector.connect(host="localhost", database="products",
                               user="root", password="")

cursor = conn.cursor()

qry = """
create table products(
prodid varchar(8) PRIMARY KEY,
prodname varchar(50) not null,
category varchar(50) not null,
price double not null
)
"""
cursor.execute(qry)

conn.close()
