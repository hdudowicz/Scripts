import pypyodbc as pyodbc
import pprint
from collections import Counter

db_host = 'DESIGNER1\INTRANET'
db_name = 'intranet'
db_user = 'intranet'
db_password = 'bathcountry110'
connection_string = 'Driver={SQL Server};Server=' + db_host + ';Database=' + db_name + ';UID=' + db_user + ';PWD=' + db_password + ';'
db = pyodbc.connect(connection_string)
cursor = db.cursor()
pp = pprint.PrettyPrinter(indent=4)

cursor.execute('SELECT * from prod_parent')

columns = [column[0] for column in cursor.description]

parentids = []

parentMTs = [[], []]

def checkEqual(iterator):
    iterator = iter(iterator)
    try:
        first = next(iterator)
    except StopIteration:
        return True
    return all(first == rest for rest in iterator)

def majority_element(lst):
    data = Counter(lst)
    return max(lst, key=data.get)

for row in cursor.fetchall():
    parentids.append(row[0])

file = open('NULL Parents.txt','w')

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
            parentMTs[0].append(id)
            parentMTs[1].append(majority_element(childrows)[24])
            break
        else:
            if childrow[24] == 'NULL' or childrow[24] == '':
                file.write(id)
            parentMTs[1].append(childrow[24])
            parentMTs[0].append(id)
            break

    # # Iterate up until id 1000
    # if id >= 1000:
    #     break

i = 0
for id in parentMTs[0]:
    if parentMTs[1][i] != None:
        cursor.execute('UPDATE prod_parent SET modern_traditional = \'' + parentMTs[1][i] + '\' WHERE displayproduct = 1 AND parentid = '+str(id))
    i += 1
cursor.commit()

print(parentMTs)
print(len(parentMTs[0]))

file.close()
cursor.close()
db.close()