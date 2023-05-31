import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh
import json


import numpy as np 

st.set_page_config(page_title="Market Sales Dashboard", page_icon=":bar_chart:", layout="wide")

st.sidebar.header("Please Filter Here:")




city = st.sidebar.multiselect(
    "Select the City:",
    options="City",
    default="City",
)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",
    options="City",
    default="City",
)

gender = st.sidebar.multiselect(
    "Select the Gender:",
    options="City",
    default="City",
)


# ---- MAINPAGE ----
st.title(":bar_chart: Market Sales Dashboard")
st.markdown("##")

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Total Sales:")
with middle_column:
    st.subheader("Average Rating:")
with right_column:
    st.subheader("Average Sales Per Transaction:")

left_column, right_column = st.columns(2)







with left_column:
    st.subheader("Filtred Data:")



st_autorefresh(interval=20000, limit=100, key="dataframe")

