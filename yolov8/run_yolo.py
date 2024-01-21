from ultralytics import YOLO
from PIL import Image

def run_yolo(yolo, image_url, save_path, conf=0.25, iou=0.7):
    results = yolo(image_url, conf=conf, iou=iou)
    res = results[0].plot()[:, :, [2,1,0]]
    image = Image.fromarray(res)
    image.save(save_path)
    return image
    
yolo = YOLO('runs/detect/train15/weights/best.pt')

image_url = 'data/test_1.jpg'
save_path = 'data/processed_test_1.jpg'
run_yolo(yolo, image_url, save_path)