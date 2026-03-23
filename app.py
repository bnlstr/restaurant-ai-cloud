import streamlit as st
from pipeline import run_pipeline

st.title("Restaurant Prospect AI")

if st.button("Run Pipeline (Fetch Latest Data)"):

    with st.spinner("Fetching and processing data..."):

        df = run_pipeline()

        st.session_state["results"] = df

        st.success(f"{len(df)} prospects found")

if "results" in st.session_state:

    st.dataframe(st.session_state["results"])
