from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# 브라우저는 cross origin이 막혀 있다.
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["http://192.168.40.105:5500/prj04/index.html"],
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],

)

@app.get("/book")
def select_book():
    print("select_book called ~~~ ")
    return {
        "title" : "Happy Birthday",
        "price" : 23000 ,
        "text": "선생님 탄생일축하드립니다!!!!"

    }