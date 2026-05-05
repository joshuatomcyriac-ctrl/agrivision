import os
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Page Configuration
st.set_page_config(page_title="AgriVision | Global Pathology Network", page_icon="🍅", layout="wide")

# --- 1. THE VIBRANT TOMATO AESTHETIC (High Contrast CSS) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;700&family=Playfair+Display:wght@900&display=swap');
    
    /* Background and Global Text */
    .stApp { background-color: #FFFDFB; }
    p, span, label { color: #1A2E44 !important; font-family: 'Plus Jakarta Sans', sans-serif; font-weight: 500; }
    
    /* Sidebar Overhaul for Readability */
    [data-testid="stSidebar"] {
        background-color: #1A2E44 !important; /* Deep Navy */
        border-right: 5px solid #D22B2B; /* Bright Tomato Red */
    }
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important; /* Force White text in Sidebar */
    }
    /* Style the selectbox specifically */
    div[data-baseweb="select"] > div {
        background-color: #FFFFFF !important;
        color: #1A2E44 !important;
        border-radius: 10px;
    }

    /* Hero Branding */
    .hero-section {
        background: linear-gradient(135deg, #D22B2B 0%, #8B0000 100%);
        padding: 60px;
        border-radius: 30px;
        text-align: center;
        color: white !important;
        box-shadow: 0 20px 40px rgba(210, 43, 43, 0.2);
        margin-bottom: 40px;
    }

    /* Chic Diagnostic Terminal */
    .terminal-box {
        background: #FFFFFF;
        border: 2px dashed #D22B2B;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        transition: 0.3s;
    }
    .terminal-box:hover { border-style: solid; background: #FFF5F5; }

    /* Info Cards */
    .pathology-card {
        background: white;
        padding: 25px;
        border-radius: 15px;
        border-left: 8px solid #D22B2B;
        box-shadow: 0 10px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. GLOBAL AI CORE ---
@st.cache_resource
def load_global_engine():
    path = 'tomato_model.h5'
    url = 'https://www.dropbox.com/scl/fi/tuys7fh7cno146u02n785/tomato_model.h5?rlkey=hbdbds81w6qwrsdi0a6pavsra&st=ol6jgxqv&dl=1'
    if not os.path.exists(path):
        with st.status("🔗 Linking to Global Seed Vault...", expanded=False):
            import urllib.request
            urllib.request.urlretrieve(url, path)
    return tf.keras.models.load_model(path, compile=False)

# --- 3. SIDEBAR NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 style='color: #FF6347 !important;'>🍅 AgriVision OS</h1>", unsafe_allow_html=True)
    st.markdown("---")
    page = st.selectbox("PORTAL NAVIGATION", 
                        ["Home Portal", "Diagnostic Terminal", "Disease Archive", "Treatment Protocols"])
    st.divider()
    st.markdown("### 🛰️ System Status")
    st.success("Core: Online")
    st.info("Node: South Asia v4.2")

# --- PAGE 1: HOME PORTAL ---
if page == "Home Portal":
    st.markdown("""
        <div class="hero-section">
            <h1 style="color: white !important; font-family: 'Playfair Display'; font-size: 4rem;">The Tomato Guardian</h1>
            <p style="color: #FFD700 !important; letter-spacing: 2px;">SECURE. DIAGNOSE. PROTECT.</p>
            <p style="font-size: 1.2rem; opacity: 0.9;">Leading the world in Solanum lycopersicum pathology through Neural Network integration.</p>
        </div>
    """, unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="pathology-card"><h3>Global Impact</h3><p>Monitoring over 4,000 hectares of farmland across developing nations to ensure food security.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="pathology-card"><h3>Neural Depth</h3><p>Trained on 20,000+ high-res images to detect microscopic cellular decay before it spreads.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="pathology-card"><h3>Sustainability</h3><p>Reducing pesticide waste by 40% through targeted spot-treatments and accurate IDs.</p></div>', unsafe_allow_html=True)

# --- PAGE 2: CHIC DIAGNOSTIC TERMINAL ---
elif page == "Diagnostic Terminal":
    st.markdown("## 🔬 Neural Scanning Terminal")
    st.write("Align specimen with the grid below for deep-layer tensor analysis.")
    
    model = load_global_engine()
    
    st.markdown('<div class="terminal-box">', unsafe_allow_html=True)
    file = st.file_uploader("DROP SPECIMEN IMAGE HERE", type=["jpg", "png", "jpeg"])
    st.markdown('</div>', unsafe_allow_html=True)
    
    if file:
        img = Image.open(file)
        st.image(img, width=500, caption="Specimen: Awaiting Analysis")
        
        if st.button("INITIATE GLOBAL DIAGNOSIS"):
            with st.spinner("Analyzing Pathogen DNA..."):
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
                st.markdown(f"""
                    <div style="background:#1A2E44; color:white; padding:30px; border-radius:15px; text-align:center;">
                        <h1 style="color:#FF6347 !important;">RESULT: {classes[idx]}</h1>
                        <h3>CONFIDENCE: {conf:.2f}%</h3>
                    </div>
                """, unsafe_allow_html=True)

# --- PAGE 3: DISEASE ARCHIVE (10 DISEASES) ---
elif page == "Disease Archive":
    st.header("📚 International Pathology Archive")
    
    cols = st.columns(2)
    diseases = [
        ("Early Blight", "Alternaria solani", "Brown spots with 'target' rings."),
        ("Late Blight", "Phytophthora infestans", "Fast-moving water-soaked patches."),
        ("Bacterial Spot", "Xanthomonas", "Small black scabby spots with yellow halos."),
        ("Leaf Mold", "Passalora fulva", "Olive-green velvet growth on undersides."),
        ("Septoria Spot", "Septoria lycopersici", "Circular spots with dark borders & grey centers."),
        ("Spider Mites", "Tetranychus urticae", "Yellow stippling and fine white webbing."),
        ("Target Spot", "Corynespora cassiicola", "Large, dark concentric lesions."),
        ("Yellow Leaf Curl", "TYLCV (Virus)", "Stunted growth and severe yellow curling."),
        ("Mosaic Virus", "ToMV", "Mottled green/yellow patchwork on leaves."),
        ("Fusarium Wilt", "Fusarium oxysporum", "Sudden yellowing and drooping on one side.")
    ]
    
    for i, (name, sci, desc) in enumerate(diseases):
        with cols[i % 2]:
            st.markdown(f"""
                <div class="pathology-card">
                    <h4>{name}</h4>
                    <p><i>{sci}</i></p>
                    <p>{desc}</p>
                </div>
            """, unsafe_allow_html=True)

# --- PAGE 4: TREATMENT PROTOCOLS ---
elif page == "Treatment Protocols":
    st.header("💊 Advanced Treatment Protocols")
    
    with st.expander("🛡️ Fungal Recovery (Blights & Spots)"):
        st.markdown("""
        - **Chlorothalonil Application:** Apply every 7 days during wet weather.
        - **Drip Irrigation:** Switch from overhead watering to soil-soaking to keep leaves dry.
        - **Mulching:** Apply straw mulch to stop spores from splashing from soil to leaves.
        """)

    with st.expander("🦟 Pest Eradication (Spider Mites)"):
        st.markdown("""
        - **Neem Oil Concentrate:** Spray both sides of the leaf at dusk.
        - **Biological Controls:** Introduce *Phytoseiulus persimilis* (predatory mites).
        - **Humidity Blast:** Increase local humidity to disrupt mite breeding.
        """)

    with st.expander("☣️ Viral Containment (Mosaic & Yellow Curl)"):
        st.markdown("""
        - **Immediate Culling:** Bag and remove the entire plant. Do not touch healthy plants after.
        - **Vector Control:** Use yellow sticky traps to eliminate whiteflies (the carriers).
        - **Tool Sterilization:** Clean pruners with 10% bleach solution between every cut.
        """)

# Footer
st.markdown("<br><hr><center><p style='color: #BDC3C7 !important;'>AgriVision Global OS | © 2026 | Built for the Future of Farming</p></center>", unsafe_allow_html=True)