import streamlit as st
import pandas as pd
import requests
from streamlit_autorefresh import st_autorefresh
import json
import numpy as np 

from keras.models import model_from_json
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input, decode_predictions

st.set_page_config(page_title="Poser votre question", layout="wide")

st.sidebar.header("Choisissez les tags:")
init_options = [" "]



if 'options' not in st.session_state:
    st.session_state.options = init_options
if 'default' not in st.session_state:
    st.session_state.default = []


ms = st.sidebar.multiselect(
    label='Pick a number',
    options=st.session_state.options,
    default=st.session_state.default
)

# If 1 is selected, remove the 2 and rerun.
if 1 in ms:
    if 2 in st.session_state.options:
        st.session_state.options.remove(2)
        st.session_state.default = ms
        st.experimental_rerun()

# Else if 2 is selected, remove the 1 and rerun.
elif 2 in ms:
    if 1 in st.session_state.options:
        st.session_state.options.remove(1)
        st.session_state.default = ms
        st.experimental_rerun()


st.write('##### Valid Selection')
st.write(str(ms))
#st_autorefresh(interval=2000, limit=100, key="dataframe")
