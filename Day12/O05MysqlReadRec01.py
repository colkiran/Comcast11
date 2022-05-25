
import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="",
                               database="products")

cursor = conn.cursor()

qry = "select * from products"

cursor.execute(qry)

for row in cursor.fetchall():
    for rec in row:
        # print(rec, end=" ")
        print("{rc:<15}".format(rc=rec), end=" ")
    print()


conn.close()
