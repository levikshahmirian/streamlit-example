import streamlit as st
import pandas as pd
import requests

import json
from urllib.error import URLError
from streamlit_autorefresh import st_autorefresh
from streamlit_elements import elements, mui, html, sync,editor, lazy,nivo

import numpy as np 

st.set_page_config(page_title="Market Sales Dashboard", page_icon=":bar_chart:", layout="wide")


# Function that fetch all data from snowflake table 




st.sidebar.image(
            "https://mail.google.com/mail/u/0?ui=2&ik=f84a0aba7a&attid=0.1&permmsgid=msg-f:1751659840764464914&th=184f255830154f12&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ9MhmfflXcF02tA97hulNBaLi8lPU9KhZ-nmoiOaK7jzKLWhvQKX0HntrVgz060igt8PIgAlq67QA1VcRGbTbgVepyHwed_J6PwrX71ytzrDgckUXZrOhjFepU&disp=emb",
            width=200, # Manually Adjust the width of the image as per requirement
        )
st.sidebar.header("Please Filter Here:")

st.markdown(
    """
<style>
span[data-baseweb="tag"] {
  background-color: #4b84ec !important;
}
</style>
""",
    unsafe_allow_html=True,
)
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



st.markdown("##")



st.markdown("""---""")



# SALES BY PRODUCT LINE [BAR CHART]
sales_by_product_line = (
    
)


# SALES BY HOUR [BAR CHART]




left_column, right_column = st.columns(2)







with left_column:
    st.subheader("Filtred Data:")


pd.set_option('display.max_rows', None)  # Display all rows
pd.set_option('display.max_columns', None)  # Display all columns
pd.set_option('display.width', 1000)  # Set the width of the display
pd.set_option('display.precision', 2)  # Set the precision of floating-point numbers



st_autorefresh(interval=20000, limit=100, key="dataframe")

st.markdown( 
   f""" 
   <style> 
   .reportview-container .main .block-container{{ 
      max-width: 800px; 
      padding-top: 3rem; 
      padding-right: 1rem; 
      padding-left: 1rem; 
      padding-bottom: 3rem; 
      }} 
      </style> """, 
      unsafe_allow_html=True 
      )