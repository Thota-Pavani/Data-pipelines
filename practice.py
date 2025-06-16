import pyodbc
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=THOTAPAVANI\SQLEXPRESS;'
    'DATABASE=customers_db;'
    'UID=sa;'
    'PWD=sql123'
)
cursor = conn.cursor()
cursor.execute("select top 5 * from olist_customers_dataset")
for row in cursor.fetchall():
    print(row)
conn.close()