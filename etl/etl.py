import pyodbc

# We are not guaranteed to run ETL AFTER the db is created.
# So we connect to master db first

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=sqlserver;"
    "DATABASE=master;"
    "UID=sa;"
    "PWD=Vjezbe123!;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()
# Using the test_init db
cursor.execute("USE test_init")

# Example ETL: add a row
cursor.execute("""
INSERT INTO fTest (LastName, FirstName)
VALUES ('TestLast', 'TestFirst')
""")

conn.commit()
conn.close()

print("ETL complete")