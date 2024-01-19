# screw-detection

env
```
pip install -r requirements.txt 
```

train
```
cp -r data/* yolov5/data/
cd yolov5
python train.py --data data/data.yaml --weights yolov5s.pt --epochs 200
```

test
```
python detect.py --source data/images/〇〇.jpg --weights runs/train/exp/weights/best.pt
```

real-time
```
python detect.py --source 0 --weights yolov5m.pt
```

sample-image

<img src="yolov5/runs/detect/exp2/test_1.jpg" width="400">
