---
title: Real Estate Price Prediction
emoji: 🏠
colorFrom: blue
colorTo: green
sdk: streamlit
sdk_version: 1.41.0
app_file: Home.py
pinned: false
license: mit
---

# Real Estate Price Prediction

A multi-page Streamlit web application for Gurgaon real estate market analysis, price prediction, and apartment recommendation.

---

## Features

| Page | Description |
|------|-------------|
| **Price Predictor** | Predicts property price (in Crores) based on user inputs using a trained ML pipeline |
| **Analytics** | Interactive visualizations — geo maps, word clouds, scatter plots, pie charts, and box plots |
| **Recommend Apartments** | Finds nearby properties within a radius and recommends similar apartments using cosine similarity |

---

## Tech Stack

- **Frontend:** Streamlit
- **ML / Data:** scikit-learn, pandas, NumPy, pickle
- **Visualization:** Plotly Express, Matplotlib, Seaborn, WordCloud
- **Dataset:** Gurgaon real estate listings with sector-level geo data

---

## Project Structure

```
CapstoneProject/
├── Home.py                          # Landing page
├── pages/
│   ├── Price Predictor.py           # ML-based price prediction
│   ├── Analysis App.py              # Data analytics & visualizations
│   └── 3_Recommend Appartments.py   # Location search & apartment recommender
├── datasets/
│   ├── data_viz1.csv                # Cleaned dataset for visualizations
│   ├── feature_text.pkl             # Feature text for word cloud
│   ├── location_distance.pkl        # Inter-property distance matrix
│   ├── cosine_sim1.pkl              # Cosine similarity matrix (amenities)
│   ├── cosine_sim2.pkl              # Cosine similarity matrix (features)
│   └── cosine_sim3.pkl              # Cosine similarity matrix (price/location)
├── df.pkl                           # Processed dataframe for dropdowns
├── pipeline.pkl                     # Trained ML pipeline (stored via Git LFS)
└── README.md
```

---

## How It Works

### Price Predictor
Takes user inputs — property type, sector, BHK, bathrooms, balconies, age, area, furnishing, luxury category, and floor — and feeds them into a serialized scikit-learn pipeline to predict price with a ±0.22 Cr confidence band.

### Analytics Dashboard
- **Geo Map:** Sector-wise average price per sqft plotted on an interactive map
- **Word Cloud:** Most common amenities/features across listings
- **Area vs Price:** Scatter plot colored by BHK count
- **BHK Distribution:** Sector-level pie chart
- **Price Range:** Box plot comparing price ranges across BHK types
- **Property Type Distribution:** KDE histogram comparing flats vs houses

### Apartment Recommender
- **Radius Search:** Lists all properties within a user-specified radius (km) from a selected location
- **Similar Properties:** Uses a weighted combination of 3 cosine similarity matrices to recommend the top 5 most similar apartments

---

## Installation & Setup

```bash
# 1. Clone the repository
git clone https://github.com/Xavier-Numbus/Real-Estate-price-prediction-.git
cd Real-Estate-price-prediction-

# 2. Install Git LFS (required for pipeline.pkl)
git lfs install
git lfs pull

# 3. Create a virtual environment
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate

# 4. Install dependencies
pip install streamlit pandas numpy scikit-learn plotly wordcloud matplotlib seaborn

# 5. Run the app
streamlit run Home.py
```

---

## Usage

1. Open the app in your browser (default: `http://localhost:8501`)
2. Use the **sidebar** to navigate between pages
3. On **Price Predictor** — fill in property details and click **Predict**
4. On **Analytics** — explore interactive charts and maps
5. On **Recommend Apartments** — enter a location and radius to search, or select an apartment for similar recommendations

---

## Dataset

The dataset covers residential properties (flats and houses) across multiple sectors in **Gurgaon, Haryana, India**. Features include:

- Property type, sector, BHK, bathrooms, balconies
- Built-up area (sq ft), property age, servant/store rooms
- Furnishing type, luxury category, floor category
- Latitude/longitude for geo-visualization
- Price (in Crores INR)

---
