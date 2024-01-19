# screw-detection

```
cp -r data/* yolov5/data/
cd yolov5
python train.py --data data/data.yaml --weights yolov5s.pt --epochs 200
```

```
python detect.py --source data/images/〇〇.jpg --weights runs/train/exp/weights/best.pt
```

Real time
```
python detect.py --source 0 --weights yolov5m.pt
```
