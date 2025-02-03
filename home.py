import streamlit as st
import sqlite3
import pandas as pd
import smtplib
import yagmail
import plotly.express as px

df = pd.read_csv("dataset\classes - Sheet1.csv")

st.title("Classes")
st.dataframe(df)
#st.map(df)

st.write("This is a line chart")
st.line_chart(df["Actual Enrollment"], x_label="Class", y_label="Enrollment")

#df_renamed = df.rename(columns={"CRN": "lat", "Term": "lon"})
#st.map(df_renamed)

st.write("slider")
x = st.slider('x')
st.write("button")
y = st.button('click me')
st.write("checkbox")
z = st.checkbox('check me')
st.write("radio")
a = st.radio('select one', [1,2,3])
st.write("selectbox")
b = st.selectbox('select one', [1,2,3])
st.write("multiselect")
c = st.multiselect('select multiple', [1,2,3])
st.write("text_input")
d = st.text_input('type here')
st.write("number_input")
e = st.number_input('enter a number')
st.write("text_area")
f = st.text_area('enter text')
st.write("date_input")
g = st.date_input('enter date')
st.write("time_input")
h = st.time_input('enter time')
st.write("file_uploader")
i = st.file_uploader('upload file')
st.write("color_picker")
j = st.color_picker('pick a color')

'''
def fetch_all_classes():
    conn = sqlite3.connect("dataset/app.db")
    df = pd.read_sql_query("SELECT * FROM records", conn)
    conn.close()
    return df
fetch_all_classes()
'''