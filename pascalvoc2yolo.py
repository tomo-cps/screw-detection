import xml.etree.ElementTree as ET

def convert_voc_to_yolo(xml_file_path, txt_file_path, class_id=0):
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    size = root.find('size')
    width = int(size.find('width').text)
    height = int(size.find('height').text)

    for obj in root.iter('object'):
        bndbox = obj.find('bndbox')
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)

        x_center = (xmin + xmax) / 2 / width
        y_center = (ymin + ymax) / 2 / height
        obj_width = (xmax - xmin) / width
        obj_height = (ymax - ymin) / height

        with open(txt_file_path, 'a') as file:
            file.write(f"{class_id} {x_center} {y_center} {obj_width} {obj_height}\n")

first_val = [i for i in range(5)]
sec_val = [i for i in range(10)]
for f in first_val:
    for s in sec_val:
        convert_voc_to_yolo('data/'+str(f)+"_"+str(s)+'.xml', str(f)+"_"+str(s)+'.txt')
