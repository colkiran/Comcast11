

import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="",
                               database="products")

cursor = conn.cursor()

qry = "delete from products where products.price < 10000"

cursor.execute(qry)

conn.commit()

conn.close()
