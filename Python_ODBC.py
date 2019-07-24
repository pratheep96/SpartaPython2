import pyodbc

class NwProducts():
    def __init__(self):
        self.server = 'localhost, 1433'
        self.database = 'Northwind'
        self.username = 'sa'
        self.password = 'Passw0rd2018'
        self.docker_Northwind = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};' + 'SERVER=' + self.server + ';DATABASE=' + self.database +';UID=' + self.username + ';PWD=' + self.password)
        self.cursor = self.docker_Northwind.cursor()

    def create(self):
        self.cursor.execute('CREATE TABLE Test (Region_ID Int, RegionDescription Varchar(255))')
        self.cursor.commit()

    def insert(self):
        self.cursor.execute("INSERT into Test (Region_ID, RegionDescription) VALUES (5, 'Southern')")
        self.cursor.commit()

    def read(self):
        result=self.cursor.execute("Select * FROM Test")
        rows = result.fetchall()
        for row in rows:
            print(row.RegionID, row.RegionDescription)

    # def delete(self):

my_db = NwProducts()
#my_db.create()
my_db.insert()
#my_db.read()