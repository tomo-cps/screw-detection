import PIL

import streamlit as st
from ultralytics import YOLO

model_path = 'weights/yolov8_epo500.pt'

st.set_page_config(
    page_title="Object Detection using YOLOv8", 
    page_icon="🤖",     
    layout="wide",      
    initial_sidebar_state="expanded"    
)

with st.sidebar:
    st.header("Image/Video Config")   
    
    image_source = st.selectbox(
        "Choose an image source", 
        ["Use default image", "Upload an image"]
    )
     
    source_img = None
    if image_source == "Upload an image":
        source_img = st.file_uploader("Upload an image...", type=("jpg", "jpeg", "png", 'bmp', 'webp'))
    else:
        source_img = 'images/test_1.jpg'

    confidence = float(st.slider(
        "Select Model Confidence", 25, 100, 40)) / 100

st.title("Object Detection using YOLOv8")

col1, col2 = st.columns(2)

with col1:
    if source_img:
        uploaded_image = PIL.Image.open(source_img)
        st.image(source_img,
                 caption="Uploaded Image",
                 use_column_width=True
                 )

try:
    model = YOLO(model_path)
except Exception as ex:
    st.error(
        f"Unable to load model. Check the specified path: {model_path}")
    st.error(ex)

if st.sidebar.button('Detect Objects'):
    res = model.predict(uploaded_image,
                        conf=confidence
                        )
    boxes = res[0].boxes
    res_plotted = res[0].plot()[:, :, ::-1]
    with col2:
        st.image(res_plotted,
                 caption='Detected Image',
                 use_column_width=True
                 )
        try:
            with st.expander("Detection Results"):
                for box in boxes:
                    st.write(box.xywh)
        except Exception as ex:
            st.write("No image is uploaded yet!")