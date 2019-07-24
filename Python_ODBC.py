import pyodbc

class NwProducts():
    def __init__(self):
        self.server = 'localhost, 1433'
        self.database = 'Northwind'
        self.username = 'sa'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' + 'SERVER=' + self.server + ';DATABASE=' + self.database +';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()


my_db = NwProducts()

result = my_db.cursor.execute('SELECT * FROM CATEGORIES')

rows = result.fetchall()
for row in rows:
    print(row.CategoryID, row.CategoryName, row.Description)


