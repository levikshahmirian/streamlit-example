import streamlit as st
import pandas as pd
import requests
import json
import numpy as np 
from keras.models import model_from_json
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input, decode_predictions

st.set_page_config(page_title="Poser votre question", layout="wide")
st.sidebar.header("Choisissez les tags:")
init_options = [""]
tags_list = [""]

# ---- MAINPAGE ----
st.title("Formation_ML Projet 5 ")
st.markdown("##")

def tags_list_change():
    init_options = tags_list


query_body = st.text_area("Ask a question about the document")
query_title = st.text_input(label="Topic (or hashtag)", placeholder="Title", on_change= tags_list_change())

def load_model(img):
    json_file = open('/app/streamlit-example/Formation_ML/model_num.json', 'r')

    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("/app/streamlit-example/Formation_ML/model_num.h5")
    #print("Loaded model from disk")

    x = preprocess_input(np.expand_dims(img.copy(), axis=0))
    preds = loaded_model.predict(x)

query_title = query_title.split(' ') 
st.session_state.options = query_title

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
