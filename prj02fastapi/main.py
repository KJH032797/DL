from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class Book(BaseModel):
    title:str
    price:int

@app.post("/book")
def create_book(book: Book):
    print(book)
    return "goooooooood"


@app.get("/hello")  # hello 주소로, get 방식으로 왔을 때 함수는 동작한다.
def hello(title:str = Form() , price: int =Form(0)):  #원래 값들은 str로 오는데, :으로 타입 힌트를 줘서 이렇게 할수 있다.
    print(f"{title} / {price}")

    print(type(title))
    print(type(price))
    print("hello called~~")

    # return "Hello World"
