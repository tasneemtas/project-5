import streamlit as st 
import pandas as pd
  
st.title("Discover Your Perfect Anime with Our Clustering Model")
st.write("""
### Today, I have created the best model for predicting your anime preferences based on the ones you've already watched.
By leveraging advanced clustering techniques, this model analyzes your viewing history and suggests the perfect anime tailored to your tastes.
Let's explore the insights generated from this model!
""")

st.subheader("Top 10 Anime Names by Score")
st.write("Here is a scatter graph showing the top 10 anime based on their scores.")

st.image('chart1.png', caption='Anime Image', use_column_width=True)
st.write("""As you can see, this chart displays the top 10 anime by score. "Sousou no Frieren" has the highest score, followed by "Fullmetal Alchemist: Brotherhood" and "Steins;Gate." The other titles are ranked accordingly, with scores ranging from 9.0 to 9.4.""")


st.subheader("Seasonal Anime ")
st.image('chart2.png', caption='Anime Image', use_column_width=True)

st.write("""
The illustration indicates that episodes with fewer than 24 are not considered seasonal, represented by the "false" segment at 18.5%. 
Episodes with 24 or more are considered seasonal, represented by the "true" segment at 81.5%.
""")


st.subheader("Top 10 Recommended Animes")
st.image('chart3.png', caption='Anime Image', use_column_width=True)

st.write("""
The data reveals the top 10 most recommended anime titles. "Death Note" takes the top spot, followed by "Steins;Gate," "Shigatsu wa Kimi no Uso," and "Fullmetal Alchemist: Brotherhood." Other popular recommendations include "Angel Beats!" and "Kimi no Na wa."
""")

st.subheader("Top 10 Not Recommended Animes")
st.image('chart4.png', caption='Anime Image', use_column_width=True)

st.write("""
The data highlights the most not recommended anime titles.
"Guilty Crown" tops the list, followed by "Domestic na Kanojo" and "B-gata H-kei." Conversely, "Isekai Cheat Magician" and "Dead Mount Death Play" have fewer avoid recommendations. This indicates that "Guilty Crown" is generally seen unfavorably, while the others may have mixed reviews.
""")

