import streamlit as st

st.set_page_config(
    page_title="Real Estate Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Real Estate Price Prediction — Gurgaon")
st.markdown("### A smart web app to explore, predict, and discover properties in Gurgaon, India")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 💰 Price Predictor")
    st.markdown(
        "Enter property details like sector, BHK, area, furnishing type, and floor — "
        "get an instant price estimate in Crores with a confidence range."
    )
    st.page_link("pages/Price Predictor.py", label="Go to Price Predictor →")

with col2:
    st.markdown("### 📊 Analytics")
    st.markdown(
        "Explore interactive visualizations — geo maps, area vs price scatter plots, "
        "BHK distribution pie charts, and property type comparisons."
    )
    st.page_link("pages/Analysis App.py", label="Go to Analytics →")

with col3:
    st.markdown("### 🔍 Recommend Apartments")
    st.markdown(
        "Find properties within a radius of any location, or get AI-powered "
        "recommendations for similar apartments based on features and pricing."
    )
    st.page_link("pages/3_Recommend Appartments.py", label="Go to Recommender →")

st.markdown("---")

st.markdown("## About the Project")

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("""
**Dataset:** Residential property listings across multiple sectors in Gurgaon, Haryana

**Features used for prediction:**
- Property type (Flat / House)
- Sector location
- Number of bedrooms, bathrooms, balconies
- Built-up area (sq ft)
- Property age, furnishing type
- Luxury category, floor category
- Servant room / Store room
""")

with col_b:
    st.markdown("""
**Tech Stack:**
- 🐍 Python
- 🎈 Streamlit
- 🤖 scikit-learn (ML Pipeline)
- 📊 Plotly, Matplotlib, Seaborn
- ☁️ WordCloud

**Model:** Trained ML pipeline using `scikit-learn` with preprocessing (encoding + scaling) and a regression model to predict log-transformed prices.

**Similarity Engine:** Weighted cosine similarity across amenities, features, and location for apartment recommendations.
""")

st.markdown("---")
st.markdown(
    "<div style='text-align:center; color:grey'>Built by Aditya Raj Kaushik &nbsp;|&nbsp; "
    "<a href='https://github.com/adityaX001/Real-Estate-price-prediction-' target='_blank'>GitHub</a></div>",
    unsafe_allow_html=True
)
