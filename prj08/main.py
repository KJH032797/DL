import oracledb
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"],
)

DB_USER = 'C##KH'
DB_PW = '1234'
DB_DSN = 'localhost:1521/xe'


def get_conn():
    conn = oracledb.connect(user=DB_USER, password=DB_PW, dsn=DB_DSN)
    return conn

class BoardCreatVo(BaseModel):
    title: str
    content: str


@app.post('/board')
def insert_board(vo: BoardCreatVo):
    print('insert board')
    conn = get_conn()
    cur = conn.cursor()

    sql = "INSERT INTO BOARD(ID, TITLE, CONTENT) VALUES(SEQ_BOARD.NEXTVAL, :t, :c)"
    sql_p = {
        't': vo.title,
        'c': vo.content
    }
    cur.execute(sql, sql_p)
    conn.commit()
    return {'message': 'board inserted'}

@app.get('/board')
def select_board_list():
    print('board_list_view')
    conn = get_conn()
    cur = conn.cursor()
    sql = "SELECT * FROM BOARD WHERE DEL_YN = 'N' ORDER BY ID DESC"
    cur.execute(sql)
    rows = cur.fetchall()
    col_list = []
    for col in cur.description:
        col_name = col[0].lower()
        col_list.append(col_name)

    data_list = []
    for row in rows:
        data = dict(zip(col_list, row))
        data_list.append(data)
    return data_list

@app.get('/board/{id}')
def select_board_by_id(id: int):
    print('board_list_detail_view')
    conn = get_conn()
    cur = conn.cursor()
    sql = "SELECT * FROM BOARD WHERE ID = :id AND DEL_YN = 'N'"
    cur.execute(sql, {'id': id})
    row = cur.fetchall()
    print(row)
    col_list = []
    for col in cur.description:
        col_name = col[0].lower()
        col_list.append(col_name)
    data = dict(zip(col_list, row))
    return data
