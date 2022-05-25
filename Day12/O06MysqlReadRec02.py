
import mysql.connector
from prettytable import PrettyTable, from_db_cursor

conn = mysql.connector.connect(host="localhost", user="root", password="",
                               database="products")

cursor = conn.cursor()

cursor.execute("select * from products")

tblObj = from_db_cursor(cursor)
tblObj.align['prodname'] = "l"
conn.close()

print(tblObj)