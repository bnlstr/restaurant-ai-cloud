import streamlit as st
import pandas as pd
from pipeline import run_pipeline

st.title("Restaurant Prospect AI")

uploaded_file = st.file_uploader("Upload Missouri Permit CSV")

if uploaded_file:

    with open("liquor_permits.csv","wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded")

if st.button("Run Pipeline"):

    with st.spinner("Processing..."):

        df = run_pipeline()

        st.session_state["results"] = df

        st.success(f"{len(df)} prospects found")

if "results" in st.session_state:

    st.dataframe(st.session_state["results"])
