# 🏠 Gurgaon Real Estate Intelligence Platform
Your AI-powered guide to property prices, market trends, and the best apartment deals in Gurgaon.

## 📌 Overview
Welcome to the **Gurgaon Real Estate Intelligence Platform** – your all-in-one tool for understanding, analyzing, and predicting property prices in one of India’s fastest-growing real estate markets.
This platform leverages **machine learning**, **data analytics**, and **interactive visualizations** to help home buyers, sellers, and real estate investors make informed, data-driven decisions.

## 🔍 Features
### 1️⃣ Home Page
- Quick overview of the Gurgaon real estate landscape.
- Intro to the platform's capabilities and how it works.
### 2️⃣ Market Analysis Dashboard
- Interactive visualizations to explore property trends in Gurgaon.
- Price distributions by **sector**, **furnishing type**, and **property type**.
- Feature importance analysis: understand what drives property prices.
- Word clouds to visualize popular amenities and features across different sectors.
### 3️⃣ Price Predictor
- Input property details like:
  - Sector
  - Bedrooms
  - Bathrooms
  - Built-up area
  - Furnishing type
- Predict the **fair market price** using our trained machine learning model.
- See how changing features (e.g., number of rooms, furnishing) impacts price.
- **Model Performance:**
  - ✅ R² Score: **90%**
  - ✅ MAE (Mean Absolute Error): **0.10**
  - 📈 Model: **XGBoost Regressor**
### 4️⃣ Apartment Recommender
- Get personalized apartment recommendations based on your preferences.
- Filter by:
  - Budget
  - Furnishing status
  - Location (Sector)
  - Features/amenities
- Discover listings offering the **best value for money** in your chosen locality.

## 🛠 How It Works
1. **Data Collection & Cleaning**  
   - Aggregated and cleaned property listing data from Gurgaon’s real estate market.
2. **Feature Engineering**  
   - Categorical, ordinal, and numerical data converted into ML-ready formats.
3. **Model Training & Interpretation**  
   - Regression models trained to predict prices.
   - Feature importance and explainability integrated.
4. **Interactive User Interface**  
   - Built with **Streamlit** for fast, responsive, and visually-rich interaction.

## 💡 Why Use This Platform?
✅ Make smarter property decisions using real-time insights.  
✅ Understand what really affects home prices in Gurgaon.  
✅ Save lakhs by knowing the true market value of properties.  
✅ Discover the best value-for-money apartments instantly.

Whether you are **buying**, **selling**, or **investing**, our platform brings **local expertise** with **global-grade analytics** right to your fingertips.
## 📊 Tech Stack
- **Frontend & UI**: Streamlit  
- **Backend & ML**: Python, Pandas, Scikit-learn  
- **Data Visualization**: Plotly, Matplotlib, WordCloud  
- **Deployment**: Streamlit Cloud / Docker (optional)

## 📍 Focus Area
**Exclusively focused on Gurgaon**, one of India’s most dynamic and evolving real estate markets.

## 🚀 Getting Started (For Developers)
### Prerequisites
- Python 3.8+
- pip
### Installation
```bash
git clone https://github.com/your-username/gurgaon-real-estate-intelligence.git
cd gurgaon-real-estate-intelligence
pip install -r requirements.txt
streamlit run app.py
