
import streamlit as st
import pandas as pd

st.title("Editable Student Table")

df = pd.DataFrame({
    "Name": ["Hema", "Anu"],
    "Roll": ["101", "102"],
    "Department": ["CSBS", "CSE"]
})

edited_df = st.data_editor(df)

st.write("Updated Table:")
st.table(edited_df)
