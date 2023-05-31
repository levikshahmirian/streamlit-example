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

query_body = st.text_area("Ask a question about the document", on_change=clear_submit)

query_title = st.text_area("Ask a question about the document", on_change=clear_submit)


button = st.button("Submit")
if button or st.session_state.get("submit"):

    if not index:
        st.error("Please upload a document!")
    elif not query_body:
        st.error("Please enter a question!")
    elif not query_title:
        st.error("Please enter a question!")
    else:
        st.session_state["submit"] = True

st_autorefresh(interval=20000, limit=100, key="dataframe")

