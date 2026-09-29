import oracledb

# select

DB_USER = 'C##KH'
DB_PW = '1234'
DB_DSN = 'localhost:1521/xe'

conn = oracledb.connect(user=DB_USER, password=DB_PW, dsn=DB_DSN)

cursor = conn.cursor()
sql = "SELECT * FROM BOARD"
cursor.execute(sql)

result = cursor.fetchall()
print(result)

cursor.close()
conn.close()