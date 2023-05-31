import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh
import json
import numpy as np 

st.set_page_config(page_title="Poser votre question", layout="wide")

st.sidebar.header("Choisissez les tags:")

def clear_submit():
    st.session_state["submit"] = False


city = st.sidebar.multiselect(
    "Selectionnez des tags:",
    options="City",
    default="City",
)

customer_type = st.sidebar.multiselect(
    "Selectionnez des Topique:",
    options="City",
    default="City",
)




# ---- MAINPAGE ----
st.title("Formation_ML Projet 5 ")
st.markdown("##")

index = None
doc = None

query = st.text_area("Ask a question about the document", on_change=clear_submit)
with st.expander("Advanced Options"):
    show_all_chunks = st.checkbox("Show all chunks retrieved from vector search")
    show_full_doc = st.checkbox("Show parsed contents of the document")

button = st.button("Submit")
if button or st.session_state.get("submit"):
    if not st.session_state.get("api_key_configured"):
        st.error("Please configure your OpenAI API key!")
    elif not index:
        st.error("Please upload a document!")
    elif not query:
        st.error("Please enter a question!")
    else:
        st.session_state["submit"] = True

st_autorefresh(interval=20000, limit=100, key="dataframe")

