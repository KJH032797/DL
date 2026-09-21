from ultralytics import YOLO

model = YOLO('best.pt')
results=model('test_images', conf=0.793, save=True) #project='D:/dev'

for r in results:
    print(r.to_json())