import pandas.io.sql
import pyodbc

# Parameters
server = 'DAVID-THINK'
db = 'BizIntel'

# Create the connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + DB['servername'] + ';DATABASE=' + DB['database'] + ';Trusted_Connection=yes')

# query db
sql = """

SELECT top 5 *
FROM data

"""
df = pandas.io.sql.read_sql(sql, conn)
print df.head()
