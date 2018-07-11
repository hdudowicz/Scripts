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


prodwb = openpyxl.load_workbook('BATHS MASTER.xlsx')
prodws = prodwb['Sheet1']

tempwb = openpyxl.load_workbook('temp.xlsx')
tempws = tempwb['Sheet1']

prodcats = []

i = 1
for sku in prodws['B']:
    # cursor.execute("SELECT * FROM prod_parent WHERE prodcode = '" + re.sub(r'/\d.?', '', str(sku.value)) + "'")
    tempws['A' + str(i)] = re.sub(r'/\d.?', '', str(prodws['B' + str(i)].value))
    i += 1
#
# i = 1
#
# for prod in prodcats:
#     print(catws['B' + str(prod)].value)
#
#     tempws['B' + str(i)] = catws['F' + str(prod)].value
#     i += 1
tempwb.save('Removed Children.xlsx')
