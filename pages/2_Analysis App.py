import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
from utils import set_background
# ----------------- PAGE CONFIG -----------------
st.set_page_config(page_title="🏙 Gurgaon Real Estate Analytics", layout="wide")
set_background("datasets/bg_city_opt.jpg", overlay_opacity=0.45)

# ----------------- PAGE TITLE -----------------
st.title("📊 Gurgaon Real Estate Analytics Dashboard")
st.markdown("Explore property prices, market distribution, and feature trends across Gurgaon sectors.")

# ----------------- LOAD DATA -----------------
new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))

numeric_cols = ['price', 'price_per_sqft', 'built_up_area', 'latitude', 'longitude']
group_df = new_df[numeric_cols + ['sector']].groupby('sector').mean()

# ----------------- GEOMAP -----------------
st.subheader("🗺 Sector Price per Sqft Geomap")
st.caption("Average price per square foot in each sector with property size bubble scaling.")
fig_map = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size='built_up_area',
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    mapbox_style="open-street-map",
    width=1200,
    height=700,
    hover_name=group_df.index
)
st.plotly_chart(fig_map, use_container_width=True)

# ----------------- FEATURE WORDCLOUD -----------------
st.subheader("☁ Features Wordcloud")
st.caption("Most frequently mentioned features in Gurgaon property listings.")

wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='white',
    stopwords=set(['s']),
    min_font_size=10
).generate(feature_text)

fig_wc, ax_wc = plt.subplots(figsize=(8, 8), facecolor=None)
ax_wc.imshow(wordcloud, interpolation='bilinear')
ax_wc.axis("off")
plt.tight_layout(pad=0)
st.pyplot(fig_wc)

# ----------------- AREA VS PRICE -----------------
st.subheader("📏 Area vs Price")
st.caption("Relationship between built-up area and price, colored by number of bedrooms.")

property_type = st.selectbox('Select Property Type', ['flat', 'house'])

df_filtered = new_df[new_df['property_type'] == property_type]
fig_area_price = px.scatter(
    df_filtered,
    x="built_up_area",
    y="price",
    color="bedRoom",
    title=f"Area vs Price ({property_type.capitalize()})",
    size_max=10
)
st.plotly_chart(fig_area_price, use_container_width=True)

# ----------------- BHK PIE CHART -----------------
st.subheader("🥧 BHK Distribution")
st.caption("Distribution of number of bedrooms (BHK) overall or by sector.")

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0, 'overall')
selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':
    fig_bhk = px.pie(new_df, names='bedRoom', title='BHK Distribution - Overall')
else:
    fig_bhk = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom', title=f'BHK Distribution - {selected_sector}')

st.plotly_chart(fig_bhk, use_container_width=True)

# ----------------- BHK PRICE BOX PLOT -----------------
st.subheader("💰 Side-by-Side BHK Price Comparison")
st.caption("Price range comparison for up to 4 BHK properties.")
fig_box = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig_box, use_container_width=True)

# ----------------- PROPERTY TYPE DISTPLOT -----------------
st.subheader("🏠 Price Distribution by Property Type")
st.caption("Distribution of property prices for houses vs flats.")

fig_dist, ax_dist = plt.subplots(figsize=(10, 4))
sns.histplot(new_df[new_df['property_type'] == 'house']['price'], label='House', kde=True, ax=ax_dist, color='orange')
sns.histplot(new_df[new_df['property_type'] == 'flat']['price'], label='Flat', kde=True, ax=ax_dist, color='blue')
ax_dist.legend()
st.pyplot(fig_dist)

# ----------------- FOOTER -----------------
st.markdown("---")
st.markdown("##### 📊 Built with Streamlit | 🧠 Powered by Machine Learning | 📍 Gurgaon Real Estate Analytics")
