import pyodbc
import os

print("ETL start")

# We connect to the master database first to establish a connection.

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=sqlserver;"
    "DATABASE=master;"
    "UID=sa;"
    "PWD=" + os.environ.get("SA_PASSWORD") + ";"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()

# Use the test_init db
cursor.execute("USE test_init")

# Example ETL: add a row to the table created during SQL Server initialization
cursor.execute("""
INSERT INTO fTest (LastName, FirstName)
VALUES ('TestLast', 'TestFirst')
""")

conn.commit()
conn.close()

print("ETL complete")