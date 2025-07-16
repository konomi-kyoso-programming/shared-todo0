import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("TO DO")
#conn = st.experimental_connection("gsheets", type="GSheetsConnection")
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="todo", ttl=5)

st.dataframe(df)

STATUS = ["DONE", "TO DO", "IN PROGRESS"]

with st.form(key="todo_form"):
    item = st.text_input(label="Item*")
    done = st.selectbox("Status", Options=STATUS)

    submit_button = st.form_submit_button(label="Submit")

if submit_buttion:
    st.write("Submission done!")