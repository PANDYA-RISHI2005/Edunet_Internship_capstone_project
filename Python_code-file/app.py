import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from utils import waste_info

model = tf.keras.models.load_model("eco_scan_model.h5")

class_names = [
'battery',
'biological',
'brown-glass',
'cardboard',
'clothes',
'green-glass',
'metal',
'paper',
'plastic',
'shoes',
'trash',
'white-glass'
]

st.set_page_config(page_title="Eco-Scan AI", page_icon="♻")

st.title("♻ Eco-Scan AI")
st.subheader("Smart Waste Detection & Recycling Assistant")

uploaded = st.file_uploader(
    "Upload Waste Image",
    type=["jpg","jpeg","png"]
)

if uploaded:

    image = Image.open(uploaded).convert("RGB")

    st.image(image, caption="Uploaded Image", width=300)

    img = image.resize((128,128))
    img = np.array(img)/255.0
    img = np.expand_dims(img, axis=0)

    prediction = model.predict(img)

    index = np.argmax(prediction)

    confidence = prediction[0][index]*100

    waste = class_names[index]

    info = waste_info[waste]

    st.success(f"Detected Waste : {waste.title()}")

    st.write("### Category")
    st.info(info["category"])

    st.write("### Disposal Bin")
    st.success(info["bin"])

    st.write("### Recycling Tip")
    st.warning(info["tip"])

    st.write("### Confidence")
    st.progress(float(confidence)/100)

    st.write(f"{confidence:.2f}%")