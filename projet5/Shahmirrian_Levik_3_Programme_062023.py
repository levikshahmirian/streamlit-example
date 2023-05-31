import streamlit as st
import pandas as pd
import requests

import json


import numpy as np 

st.set_page_config(page_title="Market Sales Dashboard", page_icon=":bar_chart:", layout="wide")

st.sidebar.header("Please Filter Here:")

left_column, middle_column, right_column = st.columns(3)

city = st.sidebar.multiselect(
    "Select the City:",

)

customer_type = st.sidebar.multiselect(
    "Select the Customer Type:",

)

gender = st.sidebar.multiselect(
    "Select the Gender:",

)


# ---- MAINPAGE ----
st.title(":bar_chart: Market Sales Dashboard")
st.markdown("##")


left_column, right_column = st.columns(2)







with left_column:
    st.subheader("Filtred Data:")



st_autorefresh(interval=20000, limit=100, key="dataframe")

