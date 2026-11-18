import oracledb

# insert

DB_USER = 'C##KH'
DB_PW = '1234'
DB_DSN = 'localhost:1521/xe'

conn = oracledb.connect(user=DB_USER, password=DB_PW, dsn=DB_DSN)

cursor = conn.cursor()

# sql = f"INSERT INTO BOARD(ID, TITLE, CONTENT) VALUES(1, 'TTT', 'CCC')"
a = input('title : ')
b = input('content : ')
# sql = f"INSERT INTO BOARD(ID, TITLE, CONTENT) VALUES(1, '{a}', '{b}')"
# cursor.execute(sql)
# conn.commit()

sql = "INSERT INTO BOARD(ID, TITLE, CONTENT) VALUES(1, :t, :c)"
sql_para = {
    "t" : a,
    "c" : b,
}
cursor.execute(sql, sql_para)
result = cursor.rowcount
print(result)
conn.commit()

cursor.close()
conn.close()
