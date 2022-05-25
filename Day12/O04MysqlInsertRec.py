
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="",
                        database="products")

cursor = conn.cursor()
# qry = "insert into products values ('PROD101', 'Laptop', 'Electronics', 67800)"
# qry = "insert into products values('PROD201', 'Desktop', 'Electronics', 57900.00)"
# qry = "insert into products values ('PROD304', 'laserjet', 'Electronics', 14250)"
# qry = "insert into products values ('PROD489', 'projector', 'Electronics', 85400)"
qry = "insert into products values ('PROD504', 'Modem', 'Electronics', 4850)"
cursor.execute(qry)

conn.commit()
conn.close()
