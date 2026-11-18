from fastapi import FastAPI,Form,UploadFile
from ultralytics import YOLO



prj_path = os.path(__file__).resolve().parent
model = YOLO("best.pt")
app = FastAPI()


@app.post("/hello")
def hello(num: int, title: str = Form()):

    print("title:", title)
    print("num:", num)



@app.get("/upload")
def upload(f: UploadFile = File()):
    print(f)


    pass