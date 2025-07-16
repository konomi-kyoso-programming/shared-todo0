import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("TO DO")
#conn = st.experimental_connection("gsheets", type="GSheetsConnection")
conn = st.connection("gsheets", type=GSheetsConnection)
df = conn.read(worksheet="sheet1", ttl=5)

st.dataframe(df)



STATUS = ["IN USE", "AVAILABLE"]

with st.form(key="the_form"):
    item = st.text_input(label="Item*")
    status = st.selectbox("Status", options=STATUS)
    entry_date = st.date_input(label="Entry date")
    
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    #st.write("Submission done!")

    if not item:
        st.warning("you must fill the item field.")
        st.stop()
    else:
        the_data = pd.DataFrame([
            {"item": item, "status": status, "entry_date": entry_date}
        ])
    updated_df = pd.concat([df, the_data], ignore_index=True)
    conn.update(worksheet="sheet1", data=updated_df)