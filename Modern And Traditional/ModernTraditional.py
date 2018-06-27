import openpyxl
import pypyodbc as pyodbc
import re

db_host = 'DESIGNER1\INTRANET'
db_name = 'intranet'
db_user = 'intranet'
db_password = 'bathcountry110'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
db = pyodbc.connect(connection_string)
cursor = db.cursor()

#Getting max parentid
cursor.execute('SELECT max(parentid) from prod_parent')

maxid = 59778

for i in range(0, maxid):
    cursor.execute('')

while True:
    row = cursor.fetchone()
    if not row:
        break


cursor.close()
db.close()