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
tags_list = []
options = st.sidebar.multiselect(
    'Choisissez dans la liste :',            
    options = tags_list,
    
    )

def clear_submit():
    st.session_state["submit"] = False

def write_predict():

    st.session_state["submit"]=True

def load_model(img):
    json_file = open('/app/streamlit-example/projet5/model_num.json', 'r')

    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("/app/projet5/Formation_ML/model_num.h5")
    #print("Loaded model from disk")


# ---- MAINPAGE ----
st.title("Formation_ML Projet 5 ")
st.markdown("##")

query_body = st.text_area("Ask a question about the document")
query_title = st.text_input(label="Topic (or hashtag)", placeholder="Title", on_change= write_predict())

doc = None


#button = st.button("Choisir des Tags")
if  st.session_state.get("submit"):

    if not query_title:
        st.error("Donnez un titre à votre question!")
    else:
        tags_list=query_title.split(" ")

if len(options) > 0:       
    st.title(options)

if st.button('Enregistrer'):
    if not query_body:
        st.error("Saisissez votre question!")
    elif not query_title:
        st.error("Donnez un titre à votre question!")
    else:
        st.write("Votre question est enregistrée !")



#st_autorefresh(interval=2000, limit=100, key="dataframe")
