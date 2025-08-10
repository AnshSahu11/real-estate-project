import streamlit as st
import pickle
import pandas as pd
import numpy as np


from utils import set_background



# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Apartment Finder",
    page_icon="🏠",
    layout="wide"
)
set_background("datasets/bg_city_opt.jpg", overlay_opacity=0.45)

# ------------------ LOAD DATA ------------------
location_df = pickle.load(open('datasets/location_distance.pkl', 'rb'))
cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl', 'rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl', 'rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl', 'rb'))

# ------------------ RECOMMENDATION FUNCTION ------------------
def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3

    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    top_properties = location_df.index[top_indices].tolist()

    return pd.DataFrame({
        'Property Name': top_properties,
        'Similarity Score': [round(s, 3) for s in top_scores]
    })

# ------------------ HEADER ------------------
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🏡 Apartment Finder & Recommender</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Find nearby apartments and get smart recommendations.</p>", unsafe_allow_html=True)
st.markdown("---")

# ------------------ LOCATION SEARCH ------------------
st.subheader("📍 Search Nearby Apartments")

col1, col2, col3 = st.columns([3, 2, 1])
with col1:
    selected_location = st.selectbox("Select Location", sorted(location_df.columns.to_list()))
with col2:
    radius = st.number_input('Radius (km)', min_value=1, max_value=50, step=1, value=5)
with col3:
    search_btn = st.button('🔍 Search')

if search_btn:
    result_ser = location_df[location_df[selected_location] < radius * 1000][selected_location].sort_values()

    if result_ser.empty:
        st.warning("⚠ No apartments found within this radius.")
    else:
        st.success(f"Found {len(result_ser)} apartments within {radius} km.")
        for key, value in result_ser.items():
            st.write(f"🏠 **{key}** — {round(value/1000, 2)} km")

st.markdown("---")

# ------------------ RECOMMENDATIONS ------------------
st.subheader("✨ Get Recommended Apartments")

col4, col5 = st.columns([4, 1])
with col4:
    selected_apartment = st.selectbox('Select an Apartment', sorted(location_df.index.to_list()))
with col5:
    recommend_btn = st.button('💡 Recommend')

if recommend_btn:
    recommendation_df = recommend_properties_with_scores(selected_apartment)
    st.write("### 🏠 Recommended Apartments")
    st.dataframe(recommendation_df.style.highlight_max(subset=["Similarity Score"], color='lightgreen'))

# ------------------ FOOTER ------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color: grey;'>Made with ❤️ using Streamlit</p>", unsafe_allow_html=True)
