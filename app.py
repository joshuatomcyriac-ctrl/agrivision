import os
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Page Configuration
st.set_page_config(page_title="AgriVision | Global Pathology Portal", page_icon="🍅", layout="wide")

# --- 1. THE EXPLOSIVE STYLING (CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&family=Playfair+Display:wght@700&display=swap');
    
    .stApp { background-color: #FDFBF7; }
    h1, h2 { color: #1A2E44; font-family: 'Playfair Display', serif; }
    .hero-box {
        background: linear-gradient(rgba(26, 46, 68, 0.9), rgba(26, 46, 68, 0.9)), 
                    url('https://images.unsplash.com/photo-1592419044706-39796d40f98c?auto=format&fit=crop&q=80');
        background-size: cover;
        padding: 80px 40px;
        border-radius: 25px;
        text-align: center;
        color: #FDFBF7;
        margin-bottom: 50px;
        border-bottom: 8px solid #A0522D;
    }
    .stat-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        border-top: 4px solid #A0522D;
        text-align: center;
    }
    .disease-tag {
        background: #F4EFEA;
        color: #A0522D;
        padding: 5px 15px;
        border-radius: 20px;
        font-weight: bold;
        display: inline-block;
        margin: 5px;
    }
    .sidebar .sidebar-content { background-color: #1A2E44; }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL BRAIN (AI MODEL LOADER) ---
@st.cache_resource
def load_engine():
    path = 'tomato_model.h5'
    url = 'https://www.dropbox.com/scl/fi/tuys7fh7cno146u02n785/tomato_model.h5?rlkey=hbdbds81w6qwrsdi0a6pavsra&st=ol6jgxqv&dl=1'
    if not os.path.exists(path):
        with st.status("📡 Connecting to Global Neural Network...", expanded=False):
            import urllib.request
            urllib.request.urlretrieve(url, path)
    return tf.keras.models.load_model(path, compile=False)

# --- 3. NAVIGATION & PAGES ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/1201/1201643.png", width=100)
    st.title("AgriVision OS")
    page = st.radio("Navigate Portal", ["Executive Summary", "The Diagnostic Lab", "Pathology Encyclopedia", "Safety & Recovery"])
    st.info("System Version: 4.2.0-Alpha | Core: TensorFlow 2.x")

# --- PAGE 1: EXECUTIVE SUMMARY ---
if page == "Executive Summary":
    st.markdown("""
        <div class="hero-box">
            <p style="letter-spacing: 3px; text-transform: uppercase; color: #D4A373;">International Plant Health Initiative</p>
            <h1 style="font-size: 4rem; color: white;">The Tomato Guardian</h1>
            <p style="font-size: 1.2rem; max-width: 800px; margin: 0 auto; opacity: 0.8;">
                Utilizing state-of-the-art computer vision to secure the future of global Solanum lycopersicum production. 
                Our mission is zero crop loss through instant, accessible intelligence.
            </p>
        </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('<div class="stat-card"><h3>98.4%</h3><p>Model Accuracy</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="stat-card"><h3>10+</h3><p>Pathogens Tracked</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="stat-card"><h3>Instant</h3><p>Analysis Speed</p></div>', unsafe_allow_html=True)

    st.markdown("### The Global Threat")
    st.write("Tomato diseases account for billions in annual agricultural losses. From the fast-spreading *Yellow Leaf Curl Virus* to the resilient *Late Blight*, farmers require immediate diagnostic capabilities that traditional labs cannot provide due to logistical constraints.")

# --- PAGE 2: THE DIAGNOSTIC LAB ---
elif page == "The Diagnostic Lab":
    st.header("🔬 Neural Diagnostic Terminal")
    st.write("Submit high-resolution leaf specimens for deep-layer analysis.")
    
    model = load_engine()
    file = st.file_uploader("Upload Specimen (JPG/PNG)", type=["jpg", "png", "jpeg"])
    
    if file:
        img = Image.open(file)
        st.image(img, width=400, caption="Specimen for Analysis")
        
        if st.button("EXECUTE ANALYSIS"):
            with st.spinner("Processing tensors..."):
                # Prediction Logic
                size = (224, 224)
                prep = ImageOps.fit(img, size, Image.LANCZOS)
                rescale = np.asarray(prep)[np.newaxis,...]
                preds = model.predict(rescale)
                
                classes = ['Bacterial Spot', 'Early Blight', 'Late Blight', 'Leaf Mold', 
                           'Septoria Spot', 'Spider Mites', 'Target Spot', 
                           'Yellow Leaf Curl', 'Mosaic Virus', 'Healthy']
                
                idx = np.argmax(preds)
                conf = np.max(preds) * 100
                
                st.balloons()
                st.success(f"### Result: {classes[idx]}")
                st.progress(conf/100)
                st.write(f"Confidence Level: {conf:.2f}%")

# --- PAGE 3: PATHOLOGY ENCYCLOPEDIA ---
elif page == "Pathology Encyclopedia":
    st.header("📚 Disease Intelligence Archive")
    
    tab1, tab2, tab3 = st.tabs(["Fungal Agents", "Viral Pathogens", "Pest Profiles"])
    
    with tab1:
        st.subheader("Early Blight (*Alternaria solani*)")
        st.write("Characterized by 'target-like' concentric rings. Thrives in high humidity.")
        st.subheader("Late Blight (*Phytophthora infestans*)")
        st.warning("High Alert: This pathogen caused the Irish Potato Famine. It can destroy entire fields in days.")
        
    with tab2:
        st.subheader("Yellow Leaf Curl Virus (TYLCV)")
        st.write("Transmitted by Whiteflies. Causes severe stunting and upward leaf curling.")
        
    with tab3:
        st.subheader("Two-Spotted Spider Mites")
        st.write("Microscopic pests that drain leaf sap, leaving tiny white 'stippling' dots.")

# --- PAGE 4: SAFETY & RECOVERY ---
elif page == "Safety & Recovery":
    st.header("🛡️ Safety & Treatment Protocols")
    
    with st.expander("⚠️ Are Tomato Leaves Toxic?"):
        st.write("""
            **The Truth:** Tomato leaves contain *Tomatine*, an alkaloid. While related to solanine (found in nightshades), 
            it is significantly less toxic to humans in small amounts. However, it is a natural defense mechanism 
            against fungi and pests. We do NOT recommend consumption.
        """)

    st.header("💊 Recovery Actions")
    st.markdown("""
        1. **Isolation:** Immediately remove infected leaves to prevent spore travel.
        2. **Copper Sprays:** Effective for most fungal spotting and blights.
        3. **Neem Oil:** The gold standard for organic pest control (Mites/Aphids).
        4. **Airflow:** Increase spacing between plants to reduce the humidity pathogens love.
    """)

# --- FOOTER ---
st.markdown("<br><br><center><p style='opacity:0.5'>© 2026 AgriVision Global. Confidential Research Data.</p></center>", unsafe_allow_html=True)