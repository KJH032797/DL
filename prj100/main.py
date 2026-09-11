from ultralytics import YOLO

# model 학습 데이터 불러오기
# m = YOLO('yolov8n.pt')
m = YOLO('./runs/detect/train/weights/best.pt')

# 학습 : 결과물 best.pt 저장
# m.train(data='./hello/data.yaml', epochs=10, imgsz=640)

# 예측
m('./abc.jpg', save=True)
