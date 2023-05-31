import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh
import json


import numpy as np 

st.set_page_config(page_title="Poser votre question", layout="wide")

st.sidebar.header("Choisissez les tags:")




city = st.sidebar.multiselect(
    "Selectionnez des tags:",
    options="City",
    default="Tags",
)

customer_type = st.sidebar.multiselect(
    "Selectionnez des Topique:",
    options="City",
    default="Topic",
)




# ---- MAINPAGE ----
st.title(":bar_chart: Formation_ML Projet 5 ")
st.markdown("##")

left_column, middle_column, right_column = st.columns(1)
with left_column:
    st.subheader("Total Sales:")









with left_column:
    st.subheader("Filtred Data:")



st_autorefresh(interval=20000, limit=100, key="dataframe")

