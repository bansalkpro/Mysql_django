# import sys
# print(sys.executable)

# import sys
# import os

# # Add a directory to the sys.path
# sys.path.append('C:\Users\PC\AppData\Local\Programs\Python\Python310\python.exe')

# # Optionally, you can also remove a directory from sys.path
# if 'C:\Python312\python.exe' in sys.path:
#     sys.path.remove('C:\Python312\python.exe')

# # Verify the changes
# print(sys.path)

import mysql.connector

dataBase = mysql.connector.connect(
	host = 'localhost',
	user = 'root',
	passwd = 'password123')
# prepare a cursor object
cursorObject = dataBase.cursor()
# Create a database
cursorObject.execute("CREATE DATABASE twdco")
print("All Done!")





