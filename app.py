import os
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Set page config for that professional feel
st.set_page_config(page_title="AgriVision | Tomato Guardian", page_icon="🍅", layout="wide")

# --- CUSTOM AESTHETIC STYLING ---
st.markdown("""
    <style>
    /* Main Background & Typography */
    .stApp {
        background-color: #FDFBF7; /* Warm Cream */
    }
    
    h1, h2, h3 {
        color: #1A2E44 !important; /* Deep Navy */
        font-family: 'Playfair Display', serif;
        font-weight: 700;
    }

    p, span, label {
        color: #2C3E50 !important;
        font-family: 'Inter', sans-serif;
    }

    /* Hero Section */
    .hero-container {
        padding: 60px 0px;
        text-align: center;
        background: linear-gradient(135deg, #1A2E44 0%, #2C3E50 100%);
        border-radius: 20px;
        margin-bottom: 40px;
        color: white !important;
    }
    
    .hero-title {
        font-size: 3.5rem;
        color: #FDFBF7 !important;
        margin-bottom: 10px;
    }

    .hero-subtitle {
        font-size: 1.2rem;
        color: #D4A373 !important; /* Muted Gold/Sienna accent */
        letter-spacing: 2px;
        text-transform: uppercase;
    }

    /* Disease Grid */
    .disease-card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        border-left: 5px solid #A0522D; /* Burnt Sienna */
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Upload Button Styling */
    .stButton>button {
        background-color: #A0522D !important;
        color: white !important;
        border-radius: 8px !important;
        border: none !important;
        padding: 10px 25px !important;
        transition: 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1A2E44 !important;
        transform: translateY(-2px);
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. THE AI ENGINE (The fixed backend) ---
@st.cache_resource
def load_optimized_model():
    model_path = 'tomato_model.h5'
    dropbox_url = 'https://www.dropbox.com/scl/fi/tuys7fh7cno146u02n785/tomato_model.h5?rlkey=hbdbds81w6qwrsdi0a6pavsra&st=ol6jgxqv&dl=1'
    
    if not os.path.exists(model_path):
        with st.status("Initializing Neural Engine...", expanded=True) as status:
            try:
                import urllib.request
                urllib.request.urlretrieve(dropbox_url, model_path)
                status.update(label="Engine Online", state="complete")
            except Exception as e:
                st.error(f"System Offline: {e}")
                return None
    try:
        return tf.keras.models.load_model(model_path, compile=False)
    except Exception as e:
        st.error(f"Loading Error: {e}")
        return None

model = load_optimized_model()

# --- 2. WELCOME / HERO SECTION ---
st.markdown("""
    <div class="hero-container">
        <p class="hero-subtitle">Next-Gen Agricultural Intelligence</p>
        <h1 class="hero-title">Tomato Guardian AI</h1>
        <p style="color: #BDC3C7 !important;">Professional-grade diagnostics for sustainable farming.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 3. PROJECT DETAILS & SCOPE ---
col1, col2 = st.columns([1, 1])

with col1:
    st.header("The Mission")
    st.write("""
        AgriVision's **Tomato Guardian** is an AI-driven diagnostic tool designed to bridge the gap 
        between complex plant pathology and everyday farming. By utilizing deep learning, we provide 
        instant, lab-accurate identifications to prevent crop loss and promote healthier yields.
    """)

with col2:
    st.header("Scope of Diagnosis")
    with st.expander("See Tracked Diseases"):
        st.markdown("""
        - **Bacterial Spot** & **Target Spot**
        - **Early & Late Blight**
        - **Leaf Mold** & **Septoria Leaf Spot**
        - **Spider Mites** (Two-spotted)
        - **Mosaic Virus** & **Yellow Leaf Curl Virus**
        - **Healthy Baseline** (Control)
        """)

st.divider()

# --- 4. THE DIAGNOSTIC LAB (The Model Interface) ---
st.header("🌿 Digital Diagnostic Lab")
st.write("Securely upload a leaf specimen for immediate AI analysis.")

file = st.file_uploader("", type=["jpg", "png", "jpeg"])

def import_and_predict(image_data, model):
    size = (224, 224)    
    image = ImageOps.fit(image_data, size, Image.LANCZOS)
    img = np.asarray(image)
    img_reshape = img[np.newaxis,...]
    prediction = model.predict(img_reshape)
    return prediction

if file is not None:
    image = Image.open(file)
    # Centering the image display
    col_left, col_mid, col_right = st.columns([1,2,1])
    with col_mid:
        st.image(image, use_container_width=True, caption="Specimen Uploaded")
    
    if model is not None:
        with st.spinner("Analyzing cellular patterns..."):
            predictions = import_and_predict(image, model)
            class_names = [
                'Bacterial Spot', 'Early Blight', 'Late Blight', 'Leaf Mold', 
                'Septoria Leaf Spot', 'Spider Mites', 
                'Target Spot', 'Yellow Leaf Curl Virus', 'Mosaic Virus', 'Healthy'
            ]
            
            result = class_names[np.argmax(predictions)]
            confidence = np.max(predictions) * 100
            
            st.markdown(f"""
                <div style="text-align: center; padding: 20px; background-color: #1A2E44; border-radius: 10px; margin-top: 20px;">
                    <h2 style="color: #FDFBF7 !important; margin: 0;">Diagnosis: {result}</h2>
                    <p style="color: #D4A373 !important; margin: 5px;">Confidence Rating: {confidence:.2f}%</p>
                </div>
                """, unsafe_allow_html=True)
    else:
        st.error("Neural engine not found. Please reboot.")

# --- 5. MINIMAL FOOTER ---
st.markdown("<br><hr><center><p style='color: #95A5A6 !important;'>© 2026 AgriVision Lab | Modernizing Plant Pathology</p></center>", unsafe_allow_html=True)