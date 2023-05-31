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





st_autorefresh(interval=20000, limit=100, key="dataframe")

