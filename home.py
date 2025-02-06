import streamlit as st
import sqlite3
import pandas as pd
import smtplib
import yagmail
import urllib.parse
import plotly.express as px

df = pd.read_csv("dataset/classes - Sheet1.csv")

def generate_email(instructor_name):
    try:
        last, rest = instructor_name.split(',')
        last = last.strip().lower()
        first = rest.strip().split()[0].lower()  
        return f"{first}.{last}@angelo.edu"
    except Exception as e:
        return "example@angelo.edu"

df["Email"] = df["Instructor"].apply(generate_email)

departments = df["Department"].unique()
selected_department = st.selectbox("Select a Department", departments)

filtered_df = df[df["Department"] == selected_department]

columns_to_show = ["Course", "Section Title", "Instructor", "Email"]
st.dataframe(filtered_df[columns_to_show])

instructor_options = filtered_df["Instructor"].unique()
selected_instructors = st.multiselect(
    "Select Instructors to Email",
    instructor_options,
    default=list(instructor_options)  
)

selected_emails = filtered_df[filtered_df["Instructor"].isin(selected_instructors)]["Email"].unique()

recipients = ",".join(selected_emails)

if recipients:
    gmail_url = f"https://mail.google.com/mail/?view=cm&fs=1&to={urllib.parse.quote(recipients)}"
    st.markdown(
        f'<a href="{gmail_url}" target="_blank"><button style="padding:8px 16px; font-size:16px;">Compose Email via Gmail</button></a>',
        unsafe_allow_html=True
    )
else:
    st.warning("No email addresses found for the selected instructors.")


CRN = df["CRN"].unique()
selected_CRN = st.number_input('enter a CRN number')
filtered_df2 = df[df["CRN"] == selected_CRN]
st.dataframe(filtered_df2)
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
e = st.number_input('enter a CRN number')
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