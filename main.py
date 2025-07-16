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
    status = st.selectbox("Status", options=STATUS)

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    #st.write("Submission done!")

    if not item:
        st.warning("you must fill the item field.")
        st.stop()
    else:
        todo_data = pd.DataFrame([
            {"item": item, "status": status}
        ])
    updated_df = pd.concat([df, todo_data], ignore_index=True)
    conn.update(worksheet="todo", data=updated_df)