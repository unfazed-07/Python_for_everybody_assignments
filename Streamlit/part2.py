import streamlit as st
import pandas as pd

st.title("Streamlit Elements Demo")
df=pd.DataFrame({
    "Name": ["Divyash", "Bob", "Charlie", "Marty"],
    "Age": [18, 36, 57, 40],
    "Occupation": ['Engineer', "Doctor", 'Artist', "Chef"]
})
st.dataframe(df)
#Table NO 2

st.subheader("Data Editor")
st.data_editor(df)
#TABLE NO 3
st.subheader("Static Table")
st.table(df)
