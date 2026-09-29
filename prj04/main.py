
from fastapi import FastAPI, Response
from fastapi.encoders import jsonable_encoder
from starlette.responses import RedirectResponse, HTMLResponse, JSONResponse, FileResponse

app= FastAPI()

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age


@app.get("/f1")
def f01():
    print("f01 called...")
    # x=["aaa","bbb","ccc"]
    x = Person("hong",20)
    # return RedirectResponse(url="/abc", status_code=123)
    return RedirectResponse("zzz")  #이를테면, 다른 페이지로 순식간에 갔다오는 상황 - 로그인, 글 등록 등등

@app.get("/f2")
def f02():
    print("f02 called...")
    return "f02에서 응답함"

@app.get("/f3")
def f03():
    print("f03 called...")
    s="<h1>hello world</h1>"
    return HTMLResponse(s)

@app.get("/f4")
def f04():
    print("f04 called...")
    return Response(
        status_code=200,
        headers={
            "Content-Type": "text/html",
            "atk": "100",
            "speed" : "200",
            "nickname" : "asdasdasd",
        },
        media_type="text/plain",  # 미디어 타입만 써놓으면 직접 적어야 할 설정들을 좀 알아서 처리해줌.
        content="123ㅇㄹㄴ뉻ㅈㅁㄴㅇㅍㅁ",

    )


@app.get("/f5")
def f05():
    print("f5 called...")
    return JSONResponse(
        status_code=200,
        headers={"Content-Type": "application/json"},
        content={
            "x" : 100,
            "y" : 200,
        }
    )

@app.get("/f6")
def f06():
    print("f6 called...")
    x = Person("hong",20)

    return JSONResponse(    # 이렇게 입력한 후 요청하면 순수한 파이썬 객체가 나오는 중이다.
        status_code=200,
        headers={},
        content=jsonable_encoder(x)

    )


@app.get("/f7")
def f06():
    print("f7 called...")

    return FileResponse("KakaoTalk_20260911_130507000.jpg")


@app.get("/f8")
def f08(nick:str = "Guest"):
    print("f08 called...")
    s=f'''
    <h1>{nick} ! hello world~~~ </h1>
    '''


    return HTMLResponse(s)



