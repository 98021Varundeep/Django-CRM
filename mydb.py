import mysql.connector

connection =  mysql.connector.connect(
    host = 'localhost',
    user= 'root',
    passwd = '12341234'

)



cursorObject = connection.cursor()

cursorObject.execute("CREATE DATABASE crm")

print("All Done!")
