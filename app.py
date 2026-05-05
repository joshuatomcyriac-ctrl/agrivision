import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# --- 1. CONFIG & THEME (The Editorial Foundation) ---
st.set_page_config(page_title="Tomato Guardian | Editorial", page_icon="🍅", layout="wide")

# Custom CSS for Monocle/Stripe Vibes
st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Inter:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
    /* Palette: Navy: #0A192F, Cream: #FDFCF8, Sienna: #A0522D */
    :root {
        --navy: #0A192F;
        --cream: #FDFCF8;
        --sienna: #A0522D;
    }
    
    .stApp { background-color: var(--cream); color: var(--navy); font-family: 'Inter', sans-serif; }
    
    h1, h2, h3 { font-family: 'Playfair Display', serif; color: var(--navy); }
    
    /* Hero Section */
    .hero-container { padding: 100px 0; text-align: center; background: var(--navy); color: var(--cream); border-radius: 0 0 50px 50px; margin-bottom: 50px; }
    
    /* Editorial Cards */
    .service-card {
        background: white; padding: 30px; border-radius: 15px; border: 1px solid #eee;
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .service-card:hover { transform: translateY(-10px); box-shadow: 0 20px 40px rgba(10,25,47,0.1); border-color: var(--sienna); }
    
    /* Portrait Masks */
    .team-mask { width: 150px; height: 150px; border-radius: 50% 20% 50% 20%; object-fit: cover; border: 3px solid var(--sienna); }
    
    .stButton>button {
        background-color: var(--sienna); color: white; border: none; padding: 12px 30px;
        font-weight: 600; border-radius: 5px; transition: all 0.3s;
    }
    .stButton>button:hover { background-color: var(--navy); transform: scale(1.02); }
    </style>
    """, unsafe_all_tags=True)

# --- 2. AI CORE (The Bulletproof Brain) ---
@st.cache_resource
def load_guardian_ai():
    try:
        # Optimized for TF 2.16+ / Keras 3
        return tf.keras.models.load_model('tomato_model.h5', compile=False)
    except Exception:
        return None

model = load_guardian_ai()

# --- 3. THE LANDING PAGE SECTIONS ---

# HERO SECTION
st.markdown("""
    <div class="hero-container">
        <p style="text-transform: uppercase; letter-spacing: 3px; font-size: 14px; color: #A0522D;">Issue No. 01 — 2026 Edition</p>
        <h1 style="font-size: 4rem; margin: 20px 0; color: white;">The Tomato Guardian</h1>
        <p style="font-size: 1.2rem; max-width: 700px; margin: 0 auto; opacity: 0.8;">
            A sophisticated intersection of agricultural science and computer vision. 
            Preserving the future of Solanum lycopersicum through deep learning.
        </p>
    </div>
    """, unsafe_all_tags=True)

# TABS FOR NAVIGATION
tab_home, tab_ai, tab_case_studies, tab_team = st.tabs(["The Journal", "Diagnostic AI", "Case Studies", "The Collective"])

with tab_home:
    st.markdown("<br><br>", unsafe_all_tags=True)
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""<div class="service-card">
            <h3 style="color: #A0522D;">01. Early Blight</h3>
            <p>Caused by <i>Alternaria solani</i>. It manifests as dark, concentric rings on older leaves. If left unchecked, it mimics the scorched earth, destroying canopy cover.</p>
        </div>""", unsafe_all_tags=True)
        
    with col2:
        st.markdown("""<div class="service-card">
            <h3 style="color: #A0522D;">02. Late Blight</h3>
            <p>The infamous <i>Phytophthora infestans</i>. Rapidly spreading through cool, wet weather, it can turn a healthy field into a gray-black rot within days.</p>
        </div>""", unsafe_all_tags=True)
        
    with col3:
        st.markdown("""<div class="service-card">
            <h3 style="color: #A0522D;">03. Mosaic Virus</h3>
            <p>A structural disruption. It creates mottled green and yellow patterns, stunting growth and curling leaves into skeletal forms.</p>
        </div>""", unsafe_all_tags=True)

with tab_ai:
    st.markdown("<h2 style='text-align: center;'>Deploy Guardian AI</h2>", unsafe_all_tags=True)
    st.markdown("<p style='text-align: center; color: #666;'>Upload a leaf specimen for high-fidelity diagnostic analysis.</p>", unsafe_all_tags=True)
    
    if model is None:
        st.warning("Architectural Error: Model file 'tomato_model.h5' not found. Check your GitHub repository.")
    else:
        uploaded_file = st.file_uploader("", type=["jpg", "png", "jpeg"])
        
        if uploaded_file:
            c1, c2 = st.columns([1, 1])
            with c1:
                img = Image.open(uploaded_file)
                st.image(img, use_container_width=True)
            
            with c2:
                with st.spinner('Engaging Neural Engine...'):
                    # Bulletproof Preprocessing
                    size = (224, 224)
                    image_proc = ImageOps.fit(img, size, Image.Resampling.LANCZOS)
                    img_array = np.asarray(image_proc).astype(np.float32) / 255.0
                    img_array = np.expand_dims(img_array, axis=0)
                    
                    preds = model.predict(img_array)
                    classes = ['Early Blight', 'Late Blight', 'Healthy', 'Yellow Leaf Curl', 'Mosaic Virus']
                    result = classes[np.argmax(preds)]
                    score = np.max(preds) * 100
                    
                    st.markdown(f"""
                        <div style="background: white; padding: 40px; border-radius: 15px; border-left: 10px solid #A0522D;">
                            <h2 style="margin:0; color: #0A192F;">{result}</h2>
                            <p style="color: #666;">Diagnostic Confidence: {score:.2f}%</p>
                        </div>
                    """, unsafe_all_tags=True)

with tab_case_studies:
    st.header("Case Studies")
    st.write("---")
    st.markdown("""
    **Project: The Village Reach (2026)**  
    *Location: Karnataka, India*  
    Reduced crop loss by 40% in a 10-farm pilot program using our lightweight diagnostic model.
    """)
    st.image("https://images.unsplash.com/photo-1591857177580-dc82b9ac4e1e?auto=format&fit=crop&q=80&w=1000", caption="Field Implementation")

with tab_team:
    st.header("The Collective")
    st.write("The minds bridging the gap between biology and bits.")
    t1, t2 = st.columns(2)
    with t1:
        st.markdown("""
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Felix" class="team-mask">
        <h4>Lead Architect</h4>
        <p style="color: #A0522D;">11th Grade Informatics Practices</p>
        """, unsafe_all_tags=True)
    with t2:
        st.markdown("""
        <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=Aneka" class="team-mask">
        <h4>Research Lead</h4>
        <p style="color: #A0522D;">CBSE Science Division</p>
        """, unsafe_all_tags=True)

# FOOTER
st.markdown("""
    <hr>
    <div style="text-align: center; padding: 50px; color: #666; font-size: 12px;">
        <p>© 2026 TOMATO GUARDIAN | DESIGNED FOR IMPACT</p>
        <p>TWITTER / GITHUB / LINKEDIN</p>
    </div>
    """, unsafe_all_tags=True)