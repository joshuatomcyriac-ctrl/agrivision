import os
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# --- 1. CLOUD MODEL LOADER ---
@st.cache_resource
def load_optimized_model():
    model_path = 'tomato_model.h5'
    
    # PASTE YOUR DROPBOX LINK HERE - Ensure it ends with dl=1
    dropbox_url = 'https://www.dropbox.com/scl/fi/tuys7fh7cno146u02n785/tomato_model.h5?rlkey=hbdbds81w6qwrsdi0a6pavsra&st=0l6jgxqv&dl=1'
    
    if not os.path.exists(model_path):
        with st.status("Downloading model...", expanded=True) as status:
            try:
                import urllib.request
                urllib.request.urlretrieve(dropbox_url, model_path)
                status.update(label="Model downloaded successfully!", state="complete")
            except Exception as e:
                st.error(f"Vault Connection Error: {e}")
                return None

    # THESE LINES MUST START AT THE SAME LEVEL AS THE 'if' ABOVE
    try:
        return tf.keras.models.load_model(model_path, compile=False)
    except Exception as e:
        st.error(f"Model Loading Error: {e}")
        return None
# Load the model
model = load_optimized_model()