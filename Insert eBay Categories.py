import pyodbc
conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=DESIGNER1\INTRANET;"
                      "Database=intranet;"
                      "Trusted_Connection=no;"
                      "UID=intranet;"
                      "PWD=bathcountry110")

cursor = conn.cursor();

