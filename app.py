import os
import gdown
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# --- 1. CLOUD MODEL LOADER ---
@st.cache_resource
def load_optimized_model():
    model_path = 'tomato_model.h5'
    file_id = '1clHHeYFvhW8hSObWyDfkC19GDDbd3hZO'
    url = f'https://drive.google.com/uc?id={file_id}'
    
    if not os.path.exists(model_path):
        with st.spinner("Downloading AI model from Cloud Vault..."):
            try:
                gdown.download(url, model_path, quiet=False)
            except Exception as e:
                st.error(f"Cloud Connection Error: {e}")
                return None
                
    try:
        return tf.keras.models.load_model(model_path, compile=False)
    except Exception as e:
        st.error(f"Model Loading Error: {e}")
        return None

# Load the model
model = load_optimized_model()