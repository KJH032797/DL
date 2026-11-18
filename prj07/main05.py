import oracledb

# delete

DB_USER = 'C##KH'
DB_PW = '1234'
DB_DSN = 'localhost:1521/xe'

conn = oracledb.connect(user=DB_USER, password=DB_PW, dsn=DB_DSN)

cursor = conn.cursor()

dele = "DELETE BOARD WHERE ID = 1"
cursor.execute(dele)
conn.commit()
cursor.close()
conn.close()