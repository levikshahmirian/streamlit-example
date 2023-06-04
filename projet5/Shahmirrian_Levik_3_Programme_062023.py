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

def clear_submit():
    st.session_state["submit"] = False

def write_predict(prob,imagenet_class_name):
    print("Loaded model from disk")

def load_model(img):
    json_file = open('/app/streamlit-example/projet5/model_num.json', 'r')

    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("/app/projet5/Formation_ML/model_num.h5")
    #print("Loaded model from disk")

   
city = st.sidebar.multiselect(
    "Selectionnez des tags:",
    options="City",
    default="City"
)

customer_type = st.sidebar.multiselect(
    "Selectionnez des tags:",
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red']
)




# ---- MAINPAGE ----
st.title("Formation_ML Projet 5 ")
st.markdown("##")

doc = None

query_body = st.text_area("Ask a question about the document", on_change=clear_submit)

query_title = st.text_input(label="Topic (or hashtag)", placeholder="Title")


button = st.button("Submit")
if button or st.session_state.get("submit"):


    if not query_body:
        st.error("Please enter a question!")
    elif not query_title:
        st.error("Please enter a question!")
    else:
        st.session_state["submit"] = True

st_autorefresh(interval=20000, limit=100, key="dataframe")

