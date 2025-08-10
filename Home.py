import streamlit as st

from utils import set_background



# Page config
st.set_page_config(
    page_title="Gurgaon Real Estate Intelligence",
    page_icon="🏠",
    layout="wide"
)
set_background("datasets/bg_city_opt.jpg", overlay_opacity=0.45)

# Title
st.title("🏠 Gurgaon Real Estate Intelligence Platform")
st.markdown("### Your AI-powered guide to property prices, market trends, and the best apartment deals in Gurgaon.")

st.markdown("---")

# Introduction
st.subheader("📌 Overview")
st.write("""
Welcome to the **Gurgaon Real Estate Intelligence Platform** – your all-in-one tool for understanding, analyzing, and predicting property prices 
in one of India’s fastest-growing real estate markets.

Our platform combines **data analytics**, **machine learning**, and **market insights** to help buyers, sellers, and investors make informed decisions.
""")

# Sections
st.markdown("## 🔍 What's Inside")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### 1️⃣ Home Page")
    st.write("Get an overview of the Gurgaon real estate market and learn how our platform works.")

    st.markdown("### 2️⃣ Market Analysis Dashboard")
    st.write("""
    - Explore Gurgaon’s property trends with interactive visualizations.
    - See **price distribution** by sector, furnishing type, and property type.
    - Understand **feature importance** – which factors influence prices the most.
    - View **word clouds** for amenities and features in each sector.
    """)

with col2:
    st.markdown("### 3️⃣ Price Predictor")
    st.write("""
    - Input property details like **sector**, **bedrooms**, **bathrooms**, **built-up area**, **furnishing type**, and more.
    - Our **machine learning model** predicts the **fair market price** instantly.
    - See how changes in features affect the price.
    """)

    st.markdown("### 4️⃣ Apartment Recommender")
    st.write("""
    - Get personalized apartment recommendations based on your preferences.
    - Filter by budget, furnishing, location, and property features.
    - Discover properties that give the **best value for money** in your desired sector.
    """)

# How it works
st.markdown("---")
st.markdown("## 🛠 How It Works")
st.write("""
1. **Data Collection & Cleaning** – Gather property listings and market data from Gurgaon’s real estate sector, clean and preprocess the data.  
2. **Feature Engineering** – Convert categorical, ordinal, and numerical variables into machine-readable formats.  
3. **Model Training & Interpretation** – Train regression models to predict prices, with an insight module that explains feature impacts.  
4. **Interactive UI** – Powered by **Streamlit** for fast predictions and rich visualizations.
""")

# Why it matters
st.markdown("---")
st.markdown("## 💡 Why This Matters")
st.write("""
Whether you are buying, selling, or investing, knowing the **true market value** and **factors that drive prices** can save you lakhs 
and ensure you make smart, data-driven decisions.

📍 Focused exclusively on **Gurgaon**, this tool brings **local expertise with global-level analytics** to your fingertips.
""")

# Footer
st.markdown("---")
st.markdown("##### 📊 Built with Streamlit | 🧠 Powered by Machine Learning | 📍 Focused on Gurgaon Real Estate")

