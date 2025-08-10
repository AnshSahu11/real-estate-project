import streamlit as st
import pickle
import pandas as pd
import numpy as np
from utils import set_background


# Page Config
st.set_page_config(
    page_title="Gurgaon Price Predictor",
    page_icon="🏠",
    layout="centered",
)
set_background("datasets/bg_city_opt.jpg", overlay_opacity=0.45)

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f7f9fc;
        padding: 2rem;
    }
    h1, h2, h3 {
        color: #1f4e79;
    }
    .stSelectbox label, .stNumberInput label {
        font-weight: bold;
    }
.prediction-box {
    padding: 1rem;
    border-radius: 10px;
    background-color: #d4edda;     /* Light green background */
    border: 2px solid #28a745;     /* Green border */
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    color: #0b3d0b;                /* Dark green text */
    margin-top: 1.5rem;
    box-shadow: 0 0 12px rgba(40, 167, 69, 0.6); /* Green glow */
    transition: 0.3s ease-in-out;
}




    .stButton>button {
        background-color: #4caf50;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3rem;
        width: 100%;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Load data & pipeline
with open('xgb_features.pkl', 'rb') as file:
    df = pickle.load(file)

with open('xgb_best_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

# Title
st.title("🏠 Gurgaon Property Price Predictor")
st.write("Fill in the details below to estimate your property price range.")

# Input Section
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        property_type = st.selectbox('Property Type', ['flat', 'house'])
        sector = st.selectbox('Sector', sorted(df['sector'].unique().tolist()))
        bedrooms = int(st.selectbox('Number of Bedrooms', sorted(df['bedRoom'].unique().tolist())))
        bathroom = int(st.selectbox('Number of Bathrooms', sorted(df['bathroom'].unique().tolist())))
        balcony = st.selectbox('Balconies', sorted(df['balcony'].unique().tolist()))
        property_age = st.selectbox('Property Age', sorted(df['agePossession'].unique().tolist()))

    with col2:
        built_up_area = float(st.number_input('Built Up Area (sq ft)', min_value=0.0))
        Extra_room = int(st.selectbox('Number of Extra Rooms', sorted(df['extra_room'].unique().tolist())))
        furnishing_type = st.selectbox('Furnishing Type', sorted(df['furnishing_type'].unique().tolist()))
        luxury_category = st.selectbox('Luxury Category', sorted(df['luxury_category'].unique().tolist()))
        floor_category = st.selectbox('Floor Category', sorted(df['floor_category'].unique().tolist()))

# Prediction
if st.button('🔍 Predict Price'):
    data = [[property_type, sector, bedrooms, bathroom, balcony, property_age,
             built_up_area, Extra_room, furnishing_type, luxury_category, floor_category]]
    columns = ['property_type', 'sector', 'bedRoom', 'bathroom', 'balcony',
               'agePossession', 'built_up_area', 'extra_room',
               'furnishing_type', 'luxury_category', 'floor_category']

    one_df = pd.DataFrame(data, columns=columns)

    base_price = np.expm1(pipeline.predict(one_df))[0]
    low = round(float(base_price - 0.22), 2)
    high = round(float(base_price + 0.22), 2)

    st.markdown(f"""
        <div class="prediction-box">
            💰 The estimated price is between <b>{low} Cr</b> and <b>{high} Cr</b>
        </div>
    """, unsafe_allow_html=True)

