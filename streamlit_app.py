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
# top_10 = mal_df.sort_values(by='Score', ascending=False).head(10)

fig = px.scatter(top_10, x='Score', y='Name', title='Top 10 Anime Names by Score', size='Score', color='Name', 
                 color_discrete_sequence=px.colors.qualitative.Pastel)
fig.update_layout(width=800, height=500)
fig.update_xaxes(dtick=0.1, range=[8, 9.5])

st.plotly_chart(fig)
