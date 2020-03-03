import pandas as pd
import pyodbc
import sys


DB = {'servername': 'DAVID-THINK',
      'database': 'BizIntel'}

# create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['Ubuntu'] + ';DATABASE=' + DB['test_db'] + ';Trusted_Connection=yes')

# query db
sql = """

SELECT top 5 *
FROM test_db.Customers

"""
df = pd.read_sql(sql, conn)
df.head()