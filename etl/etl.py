import pyodbc
import os
from pathlib import Path

print("ETL start")

# Example log in data folder, print its contents to validate succesful import into container
example_log_path = Path("/data/example.log")

with open(example_log_path, "r") as f:
    output = [line for line in f.readlines()]
    print("\n".join(output))

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