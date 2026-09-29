import io

import cv2
from fastapi import FastAPI,Form, UploadFile, File, HTTPException, Response
from ultralytics import YOLO
from pathlib import Path
from PIL import Image

x=Path(__file__).resolve().parent
model=YOLO('best.pt')

app=FastAPI()

# @app.get("/hello/{num}")
# def hello(num:int, title:str=Form()):
#     print(title)
#     print(num)

@app.get("/test")
def test():
    print("test")
    result = model("images",
                   save=True,
                   conf=0.5,
                   exist_ok=True,
                   project=f"{x}/api_prj",
                   name="inf", )


@app.post("/predict/image")
def predict_image(f: UploadFile = File()):
    data=f.file.read()
    buffer = io.BytesIO(data)
    img = Image.open(buffer)
    img = img.convert("RGB")

    results = model(img, verbose=False)
    r=results[0]

    plotted = r.plot()

    ok, buf = cv2.imencode(".jpg",plotted)

    return Response(
        content=buf.tobytes(),
        media_type="image/jpeg",   # jpg는 jpeg의 줄임말이다. (당시 네 글자 확장자명이 안돼서 줄였던거임.)
    )


