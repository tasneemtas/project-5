import streamlit as st 
import pandas as pd
import plotly.express as px
  
st.title("Discover Your Perfect Anime with Our Clustering Model")
st.write("""
### Today, I have created the best model for predicting your anime preferences based on the ones you've already watched.
By leveraging advanced clustering techniques, this model analyzes your viewing history and suggests the perfect anime tailored to your tastes.
Let's explore the insights generated from this model!
""")

st.subheader("Top 10 Anime Names by Score")
st.write("Here is a scatter graph showing the top 10 anime based on their scores.")

st.image('chart1.png', caption='Anime Image', use_column_width=True)

