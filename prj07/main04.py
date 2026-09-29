import oracledb

# update

DB_USER = 'C##KH'
DB_PW = '1234'
DB_DSN = 'localhost:1521/xe'

conn = oracledb.connect(user=DB_USER, password=DB_PW, dsn=DB_DSN)

cursor = conn.cursor()

a = input('title : ')
edit = "UPDATE BOARD SET TITLE = ':t' WHERE ID = 1"
edit_para = {
    't' : a,
}

cursor.execute(edit, edit_para)
conn.commit()

cursor.close()
conn.close()
