import os
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Forced Page Config
st.set_page_config(page_title="AgriVision | Tomato Guardian", page_icon="🍅", layout="wide")

# --- 1. THE "HIRE ME" INSPIRED AESTHETIC (High Contrast Noir) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&family=Playfair+Display:wght@900&display=swap');
    
    /* Background & Global Text */
    .stApp { background-color: #000000 !important; }
    
    h1, h2, h3, h4, p, span, li, label, .stMarkdown {
        color: #FFFFFF !important; 
        font-family: 'Inter', sans-serif !important;
    }

    /* Sidebar Overhaul */
    [data-testid="stSidebar"] {
        background-color: #FFB300 !important; /* The Bold Orange/Gold */
        border-right: None !important;
    }
    [data-testid="stSidebar"] * {
        color: #000000 !important; /* Black text on Gold background */
        font-weight: 700 !important;
    }
    div[data-baseweb="select"] > div {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }

    /* Hero Branding */
    .hero-container {
        padding: 80px 40px;
        border-left: 15px solid #FFB300;
        margin-bottom: 50px;
    }
    .hero-title {
        font-family: 'Inter', sans-serif !important;
        font-weight: 900 !important;
        font-size: 5rem !important;
        line-height: 1 !important;
        color: #FFB300 !important;
        text-transform: uppercase;
    }
    .hero-subtitle {
        font-size: 1.5rem;
        font-weight: 400;
        max-width: 600px;
        margin-top: 20px;
        opacity: 0.8;
    }

    /* Diagnostic Terminal */
    .terminal-box {
        background: #111111;
        border: 2px solid #FFB300;
        padding: 50px;
        border-radius: 5px;
        text-align: center;
    }

    /* Info Cards */
    .disease-card {
        background: #111111;
        padding: 30px;
        border-bottom: 4px solid #FFB300;
        margin-bottom: 25px;
        transition: 0.3s;
    }
    .disease-card:hover { background: #1A1A1A; }
    .disease-card h4 { color: #FFB300 !important; text-transform: uppercase; letter-spacing: 2px; }

    /* Buttons */
    .stButton>button {
        background-color: #FFB300 !important;
        color: #000000 !important;
        font-weight: 900 !important;
        border-radius: 0px !important;
        width: 100% !important;
        border: none !important;
        padding: 15px !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL BRAIN (AI MODEL) ---
@st.cache_resource
def load_noir_engine():
    path = 'tomato_model.h5'
    url = 'https://www.dropbox.com/scl/fi/irspecuqn4rinwpyynv1m/tomato_guardian_v2.h5?rlkey=le4e2l034zw860k3mg9ljtvyx&st=t7fcan68&dl=1'
    if not os.path.exists(path):
        with st.status("Establishing Secure Connection...", expanded=False):
            import urllib.request
            urllib.request.urlretrieve(url, path)
    return tf.keras.models.load_model(path, compile=False)

# --- 3. NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 style='font-size: 2.5rem; margin-bottom:0;'>AGRIVISION</h1>", unsafe_allow_html=True)
    st.markdown("<p style='margin-top:0; opacity:0.6;'>OS V.4.2 ALPHA</p>", unsafe_allow_html=True)
    st.divider()
    page = st.selectbox("SELECT MODULE", ["HOME", "LAB", "ARCHIVE", "PROTOCOLS"])
    st.divider()
    st.write("NODE: SOUTH ASIA")
    st.write("CORE: ONLINE")

# --- PAGE 1: HOME ---
if page == "HOME":
    st.markdown("""
        <div class="hero-container">
            <h1 class="hero-title">WHAT'S STOPPING YOU FROM SAVING YOUR CROP?</h1>
            <p class="hero-subtitle">In today's agricultural world, speed is survival. We provide a modern, powerful edge over pathogens before they destroy your yield.</p>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1.5, 1])
    with col1:
        st.markdown("### ABOUT THE PROJECT")
        st.write("The Tomato Guardian is a perfectionist AI. We've spent months refining our neural architecture to ensure that every leaf scan is handled with industrial-grade precision. If you want an aesthetically pleasing and technically superior diagnostic experience, you're in the right place.")
    with col2:
        st.markdown("### DATA METRICS")
        st.write("● 98.4% Classification Accuracy")
        st.write("● 10 Global Pathogens Tracked")
        st.write("● Sub-second Latency Analysis")

# --- PAGE 2: LAB ---
elif page == "LAB":
    st.markdown("<h1 style='color:#FFB300 !important;'>DIAGNOSTIC LAB</h1>", unsafe_allow_html=True)
    model = load_noir_engine()

    st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
    file = st.file_uploader("DROP SPECIMEN FOR ANALYSIS", type=["jpg", "png", "jpeg"])
    st.markdown('</div>', unsafe_allow_html=True)

    # THIS BLOCK MUST BE INDENTED TO BE INSIDE "elif page == 'LAB':"
    if file:
        img = Image.open(file)
        st.image(img, width=500)
	if st.button("RUN NEURAL SCAN"):
            with st.spinner("Analyzing..."):
                size = (224, 224)
                prep = ImageOps.fit(img, size, Image.LANCZOS)
                rescale = np.asarray(prep)[np.newaxis, ...]
                
                # Predict using the new 9.1MB model
                preds = model.predict(rescale)
                
                classes = [
                    'Bacterial Spot', 'Early Blight', 'Late Blight', 'Leaf Mold',
                    'Septoria Spot', 'Spider Mites', 'Target Spot',
                    'Yellow Leaf Curl', 'Mosaic Virus', 'Healthy'
                ]
                
                idx = np.argmax(preds)
                conf = np.max(preds) * 100
                
                # Result display with high-contrast styling
                st.markdown(f"""
                    <div style='background:#FFB300; padding:40px; text-align:center;'>
                        <h1 style='color:black !important; margin:0;'>{classes[idx]}</h1>
                        <p style='color:black !important; font-weight:bold;'>CONFIDENCE: {conf:.2f}%</p>
                    </div>
                """, unsafe_allow_html=True)
# --- PAGE 3: ARCHIVE ---
elif page == "ARCHIVE":
    st.markdown("<h1 style='color:#FFB300 !important;'>PATHOLOGY ARCHIVE</h1>", unsafe_allow_html=True)
    diseases = [
        ("Early Blight", "Alternaria solani", "Concentric bullseye rings on older leaves."),
        ("Late Blight", "Phytophthora infestans", "Dark oily patches; can destroy a field in 7 days."),
        ("Bacterial Spot", "Xanthomonas", "Greasy black scabs with yellow halos."),
        ("Leaf Mold", "Passalora fulva", "Olive-green velvet growth on leaf undersides."),
        ("Septoria Spot", "Septoria lycopersici", "Small circular spots with grey centers."),
        ("Spider Mites", "Tetranychus urticae", "Yellow stippling and fine protective webbing."),
        ("Target Spot", "Corynespora cassiicola", "Large dark lesions mimicking a target board."),
        ("Yellow Leaf Curl", "TYLCV (Virus)", "Stunted upright growth with yellow curling."),
        ("Mosaic Virus", "ToMV", "Mosaic green/yellow patchwork; uneven ripening."),
        ("Fusarium Wilt", "Fusarium oxysporum", "Sudden yellowing and drooping of the entire plant.")
    ]
    cols = st.columns(2)
    for i, (name, sci, desc) in enumerate(diseases):
        with cols[i % 2]:
            st.markdown(f"<div class='disease-card'><h4>{name}</h4><p><i>{sci}</i></p><p>{desc}</p></div>", unsafe_allow_html=True)

# --- PAGE 4: PROTOCOLS ---
elif page == "PROTOCOLS":
    st.markdown("<h1 style='color:#FFB300 !important;'>RECOVERY PROTOCOLS</h1>", unsafe_allow_html=True)
    
    st.subheader("01. FUNGAL ATTACK")
    st.write("Apply Copper Fungicide every 10 days. Prune lower leaves to stop soil splash.")
    
    st.subheader("02. PEST INFESTATION")
    st.write("Use 1% Neem Oil solution. Introduce predatory mites like P. persimilis.")
    
    st.subheader("03. VIRAL CONTAINMENT")
    st.write("Immediate isolation and removal. Sterilize all tools with 10% bleach.")

# Footer
st.markdown("<br><br><p style='opacity:0.3; text-align:center;'>AGRIVISION GLOBAL © 2026</p>", unsafe_allow_html=True)