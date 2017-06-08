
import sys
import mysql
import mysql.connector


#database connection
orderId = sys.argv[1]
order = int(orderId)
hostname = 'localhost'
username = 'root'
password = ''
database = 'perfitdb'	

db = mysql.connector.connect( host=hostname, user=username, password=password, database=database )
cursor = db.cursor()

# Execute SQL select statement
cursor.execute('SELECT * FROM `orders_table` INNER Join user_measurement_table on user_measurement_table.scan_id = orders_table.scan_id WHERE order_id ='+orderId)

row = cursor.fetchone ()
print(row[2])

db.close()
