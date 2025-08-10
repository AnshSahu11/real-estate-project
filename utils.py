# utils.py
import streamlit as st
import base64
from pathlib import Path

def set_background(image_path: str, overlay_opacity: float = 0.45):
    """
    Sets a full-page background image from a local file and adds a dark overlay.
    image_path: relative path to image file in your project (e.g., 'images/bg_city_opt.jpg')
    overlay_opacity: 0.0 (no darkening) .. 0.8 (very dark)
    """
    img_file = Path(image_path)
    if not img_file.exists():
        st.error(f"Background image not found: {image_path}")
        return

    with open(img_file, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{b64}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        background: rgba(0,0,0,{overlay_opacity});
        z-index: 0;
        pointer-events: none;
    }}

    .block-container {{
        position: relative;
        z-index: 1;
    }}

    [data-testid="stSidebar"] {{
        background-color: rgba(8, 8, 8, 0.6) !important;
        z-index: 2;
    }}

    .stApp * {{
        color: #ffffffcc !important;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)
