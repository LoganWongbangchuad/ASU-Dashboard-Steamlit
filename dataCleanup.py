import streamlit as st
import pandas as pd

df = pd.read_csv("dataset/02-Student-Course-grades.csv", sep="|")
st.dataframe(df)

df2 = pd.read_csv("dataset/01-Student-course-mapping_clean.csv")
st.dataframe(df2)

