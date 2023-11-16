import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

st.title("Popular Names")

url = "https://raw.githubusercontent.com/esnt/Data/main/Names/popular_names.csv"

df = pd.read_csv(url)


username = st.text_input("Put First Name Here")

name_df = df[df["name"] == username]

if name_df.empty:
    st.write("Name not found")
else:
    fig = px.line(name_df, x = "year", y="n", color="sex", 
                  color_discrete_sequence = px.colors.qualitative.Set1)
    st.plotly_chart(fig)
    

useryear = st.selectbox("Select a year", df["year"].unique())

year_df = df[df["year"] == useryear]

girl_names = year_df[year_df["sex"] == "F"].sort_values(by="n", ascending = False).head(5)[["name", "n"]].reset_index(drop=True)

boy_names = year_df[year_df["sex"] == "M"].sort_values(by="n", ascending = False).head(5)[["name", "n"]].reset_index(drop=True)

st.write(f"The top girl names from {useryear} are:")
st.dataframe(girl_names)

st.write(f"The top boy names from {useryear} are:")
st.dataframe(boy_names)

