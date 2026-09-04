import streamlit as st
import pickle
import numpy as np
import pandas as pd
from streamlit import button

st.set_page_config(page_title="Recommend Appartements")

location_df = pickle.load(open('datasets/location_distance.pkl', 'rb'))

cosine_sim1 = pickle.load(open('datasets/cosine_sim1.pkl','rb'))
cosine_sim2 = pickle.load(open('datasets/cosine_sim2.pkl','rb'))
cosine_sim3 = pickle.load(open('datasets/cosine_sim3.pkl','rb'))


def recommend_properties_with_scores(property_name, top_n=5):
    cosine_sim_matrix = 0.5 * cosine_sim1 + 0.8 * cosine_sim2 + 1 * cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[location_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = location_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df


# Test the recommender function using a property name
recommend_properties_with_scores('Ireo Victory Valley')


st.title('Select Location and Radius')

selected_location = st.selectbox('Location',sorted(location_df.columns.to_list()))

radius = st.number_input("Radius in Kms")

if st.button('Search'):
     result_ser =location_df[location_df[selected_location] < radius*1000][selected_location].sort_values()

     for key, value in result_ser.items():
         st.text(str(key) + " " + str(round(value/1000)) + 'kms')

st.title('Recommend Appartements')
selected_appartement = st.selectbox(
    'Select an appartement',
    sorted(location_df.index.to_list())
)

if button('Recommend'):
    recommendation_df = recommend_properties_with_scores(selected_appartement)

    st.dataframe(recommendation_df)



#     appartment = []
#     for key, value in result_ser.items():
#         appartment.append(str(key) + " " + str(round(value/1000)) + 'kms')
#     selected_appartment = st.radio("Select anyone for recommendation",appartment)
#
#     if selected_appartment:
#         st.text('Hello')

## correct one -
# if st.button("Search"):
#     st.session_state.search_clicked = True
# if st.session_state.get("search_clicked", False):
#     result_ser = location_df[
#         location_df[selected_location] < radius * 1000
#     ][selected_location].sort_values()
#     apartment = [
#         f"{key} {round(value/1000)} kms"
#         for key, value in result_ser.items()
#     ]
#     selected_apartment = st.radio(
#         "Select anyone for recommendation",
#         apartment,
#         key="apartment_radio"
#     )
#     if selected_apartment:
#         st.success(f"You selected: {selected_apartment}")

## end -->



