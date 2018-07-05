import openpyxl
import pypyodbc as pyodbc
import re
import pprint
import numpy

db_host = 'DESIGNER1\INTRANET'
db_name = 'intranet'
db_user = 'intranet'
db_password = 'bathcountry110'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
db = pyodbc.connect(connection_string)
cursor = db.cursor()
pp = pprint.PrettyPrinter(indent=4)

#Getting max parentid
cursor.execute('SELECT max(parentid) from prod_parent')

maxid = 500

cursor.execute('SELECT * from prod_parent')

columns = [column[0] for column in cursor.description]

parentids = []

parentMTs = []
def checkEqual(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

for row in cursor.fetchall():
    parentids.append(row[0])
    # pp.pprint(dict(zip(columns, row)))
items = 0
# Iterate over all parent ids
for id in parentids:
    # Select children with parentid = id
    cursor.execute('SELECT * from prod_child where child_parentid = ' + str(id))
    childrows = []
    # Append all rows to childrows
    for row in cursor.fetchall():
        childrows.append(row)
        print(row)

    # Iterate over child rows, add M or T to parentMTs if all modern_traditional children fields are equal or 0 if not equal
    for childrow in childrows:
        if childrows.count(childrow) == len(childrows):
            parentMTs.append(0)
            items += 1
            break
        else:
            parentMTs.append(childrow[24])
            items += 1
            break
    # Iterate up until id 1000
    if id >= 1000:
        break
print(parentMTs)
print(len(parentMTs))
print('Items: ' + str(items))



cursor.close()
db.close()