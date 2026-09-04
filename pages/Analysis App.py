import streamlit as st
import pandas as pd
import plotly.express as px
import pickle
from wordcloud import WordCloud
from matplotlib import pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Analytics", layout="wide")

st.title("Analytics")

# Load data
new_df = pd.read_csv('datasets/data_viz1.csv')
feature_text = pickle.load(open('datasets/feature_text.pkl', 'rb'))
# Group by sector
group_df = (
    new_df.groupby('sector')[[
        'price',
        'price_per_sqft',
        'built_up_area',
        'latitude',
        'longitude'
    ]]
    .mean()
    .reset_index()
)
st.header("Sector Price_Per_Sqft GeoMap")
# Create map
fig = px.scatter_mapbox(
    group_df,
    lat="latitude",
    lon="longitude",
    color="price_per_sqft",
    size="built_up_area",
    hover_name="sector",
    text="sector",
    color_continuous_scale=px.colors.cyclical.IceFire,
    zoom=10,
    size_max=25,
    mapbox_style="open-street-map",
    width=1200,
    height=700
)

st.plotly_chart(fig, use_container_width=True)

#
st.header("Features WordCloud")
wordcloud = WordCloud(width = 800, height = 800,
                      background_color ='white',
                      stopwords = set(['s']),  # Any stopwords you'd like to exclude
                      min_font_size = 10).generate(feature_text)

fig, ax = plt.subplots(figsize=(8, 8))

ax.imshow(wordcloud, interpolation='bilinear')
ax.axis("off")
st.pyplot(fig)

st.header('Area Vs Price')
property_type = st.selectbox('Select Property Type', ['flat', 'house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x='built_up_area', y='price', color='bedRoom', title='Area Vs Price')
    st.plotly_chart(fig1, use_container_width=True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x='built_up_area', y='price', color='bedRoom',
                      title='Area Vs Price')
    st.plotly_chart(fig1, use_container_width=True)

st.header('BHK Pie Chart')
sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'overall')

selected_sector = st.selectbox('Select Sector', sector_options)

if selected_sector == 'overall':
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom')
    st.plotly_chart(fig2, use_container_width=True)


st.header('Side_by_Side BHK Price Comparison')
# Create side-by-side boxplot of the total bill amounts by day
fig3 = px.box(new_df[new_df['bedRoom'] <= 4], x='bedRoom', y='price', title='BHK Price Range')
# Show the plot
st.plotly_chart(fig3, use_container_width=True)



st.header('Side-by-Side Distplot for Property Type')

fig4, ax = plt.subplots(figsize=(10, 4))

sns.histplot(
    new_df[new_df['property_type'] == 'house']['price'],
    kde=True,
    label='house',
    ax=ax
)

sns.histplot(
    new_df[new_df['property_type'] == 'flat']['price'],
    kde=True,
    label='flat',
    ax=ax
)

ax.legend()

st.pyplot(fig4)
