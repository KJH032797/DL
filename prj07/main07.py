from dataclasses import dataclass

import oracledb

@dataclass
class BoardVO:
    id: int
    title: str
    content: str

def get_conn():
    DB_USER = 'C##KH'
    DB_PW = '1234'
    DB_DSN = 'localhost:1521/xe'
    return oracledb.connect(user=DB_USER, password=DB_PW, dsn=DB_DSN)

def print_menu():
    print()
    print('1. insert_board')
    print('2. update_board_title')
    print('3. delete_board_by_id')
    print('4. select_board_one')
    print('5. select_board_list')


def choose_menu():
    print_menu()
    num = int(input("\nchoose a menu number : "))
    match num:
        case 0:
            return True
        case 1:
            insert_board()
            return False
        case 2:
            update_board_title()
            return False
        case 3:
            delete_board_by_id()
            return False
        case 4:
            select_board_one()
            return False
        case 5:
            select_board_list()
            return False
        case _:
            print('invalid choice')
            return False


def insert_board():
    print('====게시글 작성====')
    conn = get_conn()
    cursor = conn.cursor()
    sql = "INSERT INTO BOARD(ID, TITLE, CONTENT) VALUES(SEQ_BOARD.NEXTVAL, :title, :content)"
    sql_p = {
        'title' : '260929class',
        'content' : 'ING'
    }
    cursor.execute(sql, sql_p)
    result = cursor.rowcount
    print(result)
    conn.commit()
    print('success')
    cursor.close()
    conn.close()

def update_board_title():
    print('on def UBT')


def delete_board_by_id():
    print('on def DBI')


def select_board_one():
    print('====게시글 상세조회====')
    id = int(input("\ninsert board id : "))
    conn = get_conn()
    cursor = conn.cursor()
    sql = "SELECT * FROM BOARD WHERE ID = :id"
    sql_p = {'id' : id}
    cursor.execute(sql, sql_p)
    row = cursor.fetchone()
    print(type(row))
    print(row)
    cursor.close()
    conn.close()


def select_board_list():
    print('====게시글 목록 조회====')
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM BOARD ORDER BY ID")
    col_name_list = []
    for col in cursor.description:
        col_name = col[0].lower()
        col_name_list.append(col_name)

    row_list = cursor.fetchall()
    vo_list = []
    for row in row_list:
        x = dict(zip(col_name_list, row))
        vo = BoardVO(**x)
        vo_list.append(vo)
    print(vo_list)

if __name__ == '__main__':
    while True:
        r = choose_menu()
        if r == True:
            break