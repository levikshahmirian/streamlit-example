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
init_options = ["1","2"]
tags_list = [" "]

# ---- MAINPAGE ----
st.title("Formation_ML Projet 5 ")
st.markdown("##")

def tags_list_change():
    init_options = tags_list

query_body = st.text_area("Ask a question about the document")
query_title = st.text_input(label="Topic (or hashtag)", placeholder="Title", on_change= tags_list_change())

st.session_state.options = query_title.tolist()

if 'options' not in st.session_state:
    st.session_state.options = init_options
if 'default' not in st.session_state:
    st.session_state.default = []

ms = st.sidebar.multiselect(
    label='Pick a number',
    options=st.session_state.options,
    default=st.session_state.default
)

st.write('##### Valid Selection')
st.write(str(ms))
