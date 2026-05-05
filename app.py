import os
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# --- 1. CLOUD MODEL LOADER ---
@st.cache_resource
def load_optimized_model():
    model_path = 'tomato_model.h5'
    
    # Dropbox link with dl=1 for direct download
    dropbox_url = 'https://www.dropbox.com/scl/fi/tuys7fh7cno146u02n785/tomato_model.h5?rlkey=hbdbds81w6qwrsdi0a6pavsra&st=ol6jgxqv&dl=1'
    
    if not os.path.exists(model_path):
        with st.status("Connecting to Vault...", expanded=True) as status:
            try:
                import urllib.request
                urllib.request.urlretrieve(dropbox_url, model_path)
                status.update(label="Model retrieved!", state="complete")
            except Exception as e:
                st.error(f"Download Error: {e}")
                return None
                
    try:
        return tf.keras.models.load_model(model_path, compile=False)
    except Exception as e:
        st.error(f"Model Loading Error: {e}")
        return None

# Trigger the load
model = load_optimized_model()

# --- 2. THE APP INTERFACE ---
st.title("🍅 Tomato Guardian: AI Disease Lab")
st.write("Upload a leaf photo to diagnose health issues instantly.")

file = st.file_uploader("Choose a tomato leaf image...", type=["jpg", "png", "jpeg"])

def import_and_predict(image_data, model):
    size = (224, 224)    
    image = ImageOps.fit(image_data, size, Image.LANCZOS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction

if file is None:
    st.text("Please upload an image file")
else:
    image = Image.open(file)
    st.image(image, use_column_width=True)
    
    if model is not None:
        predictions = import_and_predict(image, model)
        class_names = [
            'Bacterial_spot', 'Early_blight', 'Late_blight', 'Leaf_Mold', 
            'Septoria_leaf_spot', 'Spider_mites Two-spotted_spider_mite', 
            'Target_Spot', 'Tomato_Yellow_Leaf_Curl_Virus', 'Tomato_mosaic_virus', 'Healthy'
        ]
        
        string_output = "Diagnosis: " + class_names[np.argmax(predictions)]
        st.success(string_output)
    else:
        st.error("Model is not loaded. Check the sidebar/logs.")