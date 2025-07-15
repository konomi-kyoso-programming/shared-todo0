import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

st.title("TO DO")
conn = st.experimental_connection("gsheets", type="GSheetsConnection")
df = conn.read(worksheet="to-do", ttl=5)

st.dataframe(df)
