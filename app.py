import os
import streamlit as st
import tensorflow as tf
from PIL import Image, ImageOps
import numpy as np

# Forced Page Config
st.set_page_config(page_title="AgriVision | Recovery Unit", page_icon="🍅", layout="wide")

# --- 1. THE NOIR AESTHETIC (Forced High Contrast) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    
    .stApp { background-color: #000000 !important; }
    
    h1, h2, h3, h4, p, span, li, label {
        color: #FFFFFF !important; 
        font-family: 'Inter', sans-serif !important;
    }

    /* Sidebar - Bold Gold */
    [data-testid="stSidebar"] {
        background-color: #FFB300 !important;
    }
    [data-testid="stSidebar"] * {
        color: #000000 !important;
        font-weight: 900 !important;
    }

    /* Protocol Cards */
    .protocol-card {
        background: #111111;
        padding: 25px;
        border-left: 10px solid #FFB300;
        margin-bottom: 20px;
        border-radius: 0 10px 10px 0;
    }
    .protocol-num {
        color: #FFB300 !important;
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        line-height: 1;
    }
    .protocol-title {
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 700;
        margin-top: 10px;
        display: block;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 2. NAVIGATION ---
with st.sidebar:
    st.markdown("<h1 style='font-size: 2rem;'>AGRIVISION</h1>", unsafe_allow_html=True)
    st.divider()
    page = st.selectbox("PORTAL", ["HOME", "LAB", "RECOVERY PROTOCOLS"])
    st.divider()
    st.write("STATUS: ENFORCED")

# --- PAGE: HOME & LAB (Briefly kept for structure) ---
if page == "HOME":
    st.markdown("<h1 style='font-size: 4rem; color:#FFB300 !important;'>RECOVERY IS NOT OPTIONAL.</h1>", unsafe_allow_html=True)
    st.write("Access the recovery module to stabilize your crop yield through 10 industrial-grade protocols.")

elif page == "LAB":
    st.header("NEURAL SCANNING")
    st.write("Drop specimen for pathogen identification.")

# --- PAGE: 10 RECOVERY PROTOCOLS ---
elif page == "RECOVERY PROTOCOLS":
    st.markdown("<h1 style='color:#FFB300 !important; font-size: 3rem;'>THE DECAD ARCHIVE</h1>", unsafe_allow_html=True)
    st.write("A master list of 10 stabilization protocols for Solanum lycopersicum.")
    
    protocols = [
        ("Fungal Suppression", "Apply copper-based fungicides every 7–10 days; focus on undersides."),
        ("Airflow Optimization", "Prune lower 'sucker' branches to increase wind-speed between stems."),
        ("Hydraulic Correction", "Transition to drip irrigation; wet leaves are a catalyst for blight."),
        ("Pest Blitz", "Deploy 1% Neem Oil concentrate during twilight hours to suffocate mites."),
        ("Biological Warfare", "Introduce predatory mites (P. persimilis) to hunt Spider Mite colonies."),
        ("Viral Rogueing", "Immediately uproot and incinerate plants showing Mosaic patterns."),
        ("Nutrient Rebalancing", "Flush soil with 5-10-5 NPK to strengthen cellular walls against fungi."),
        ("Vector Shielding", "Install yellow sticky traps (1 per 10sqft) to capture Whitefly carriers."),
        ("Sterile Loop", "Dip all pruning tools in a 10% bleach solution between every plant cut."),
        ("Surface Mulching", "Apply organic straw mulch to create a physical barrier against soil-borne spores.")
    ]

    for i, (title, desc) in enumerate(protocols):
        st.markdown(f"""
            <div class="protocol-card">
                <span class="protocol-num">0{i+1 if i < 9 else i+1}</span>
                <span class="protocol-title">{title}</span>
                <p style="margin-top:10px; opacity:0.8;">{desc}</p>
            </div>
        """, unsafe_allow_html=True)

# Footer
st.markdown("<br><hr><center>© 2026 AGRIVISION UNIT</center>", unsafe_allow_html=True)