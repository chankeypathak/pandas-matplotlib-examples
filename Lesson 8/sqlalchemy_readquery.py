from sqlalchemy import create_engine

# Parameters
ServerName = "DAVID-THINK"
Database = "BizIntel"
Driver = "driver=SQL Server Native Client 11.0"

# Create the connection
engine = create_engine('mssql+pyodbc://' + ServerName + '/' + Database + "?" + Driver)

df = pd.read_sql_query("SELECT top 5 * FROM data", engine)
print df