# screw-detection

1. env
```
pip install -r requirements.txt 
```
2. create yolov5/data/data.yaml
``` data.yaml
train: data/train/images
val: data/valid/images

nc: 5
names: ['screw0', 'screw1', 'screw2', 'screw3', 'screw4']
```

3. train/valid
```
cp -r data/* yolov5/data/
cd yolov5
python train.py --data data/data.yaml --weights yolov5s.pt --epochs 200
```

4. test
```
python detect.py --source data/images/〇〇.jpg --weights runs/train/exp/weights/best.pt
```

5. real-time
```
python detect.py --source 0 --weights yolov5m.pt
```

sample-image

<img src="yolov5/runs/detect/exp2/test_1.jpg" width="400">
