# screw-detection
This repository is a task to detect screws using YOLO. You can experiment with the screws you want to detect :fire:

## 1. Create Dataset
### 1.1 Take some images for object detection
- 10 shots of 5 classes of screws each

### 1.2 Annotate with [LabelImg](https://github.com/HumanSignal/labelImg), an image annotation tool.
```
pip3 install labelImg
labelImg
```

## 2. Training with YOLO
### 2.1 Environment building

```
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt 
```
### 2.2 Split the created data into training(80%) and validation(20%) data, and place data for each.
```
.
├── README.md
├── data
└── yolov5
    ├── data
    │   ├── data.yaml
    │   ├── test_1.jpg
    │   ├── train
    │   │   ├── images
    │   │   │   ├── 0_0.jpg
    │   │   │   ├── 0_1.jpg
    │   │   │   ├── 0_2.jpg
    │   │   │   ├── 0_3.jpg
                       ・
                       ・
    │   │   ├── labels
    │   │   │   ├── 0_0.txt
    │   │   │   ├── 0_1.txt
    │   │   │   ├── 0_2.txt
    │   │   │   ├── 0_3.txt
                       ・
                       ・
    │   ├── valid
    │   │   ├── images
    │   │   │   ├── 0_8.jpg
    │   │   │   ├── 0_9.jpg
                       ・
                       ・
    │   │   ├── labels
    │   │   │   ├── 0_8.txt
    │   │   │   ├── 0_9.txt
                       ・
                       ・
    ├── requirements.txt
```

### 2.3 Create yolov5/data/data.yaml
``` data.yaml
train: data/train/images
val: data/valid/images

nc: 5 # number of classes
names: ['screw0', 'screw1', 'screw2', 'screw3', 'screw4'] # class name
```

### 2.4 Start of training and validation
```
cp -r data/* yolov5/data/
cd yolov5
python train.py --data data/data.yaml --weights yolov5s.pt --epochs 200
```

### 2.5 Test
```
python detect.py --source data/images/〇〇.jpg --weights runs/train/exp/weights/best.pt
```

### 2.6 Real-time
```
python detect.py --source 0 --weights yolov5m.pt
```

- sample-image

<img src="yolov5/runs/detect/exp2/test_1.jpg" width="400">
