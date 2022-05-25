
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="",
                               database="products")

cursor = conn.cursor()

qry = "update products set price = price + (price * 0.1) where category = 'electronics'"

cursor.execute(qry)

conn.commit()

conn.close()
