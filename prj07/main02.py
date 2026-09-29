import oracledb

DB_USER = 'C##KH'
DB_PW = '1234'
DB_DSN = 'localhost:1521/xe'

conn = oracledb.connect(user=DB_USER, password=DB_PW, dsn=DB_DSN)

print(conn.version)