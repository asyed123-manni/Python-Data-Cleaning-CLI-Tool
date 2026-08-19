import streamlit as st
import pandas as pd

st.title("Data Cleaning Tool")
file = st.file_uploader("Upload CSV", type=["csv"])

if file is not None:
    df = pd.read_csv(file)
    st.write("### Raw Data", df)
    cleaned_df = df.fillna(df.median(numeric_only=True))
    st.write("### Cleaned Data", cleaned_df)
    st.download_button("Download Cleaned CSV", cleaned_df.to_csv(index=False), "clean.csv")
