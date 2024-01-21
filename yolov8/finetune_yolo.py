from ultralytics import YOLO

yolo = YOLO('yolov8n.pt')
yolo.train(data='data/data.yaml', epochs=500, patience=0)
valid_results = yolo.val()
print(valid_results)