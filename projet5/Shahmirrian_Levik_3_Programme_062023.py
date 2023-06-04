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


tags_list = []
def clear_submit():
    st.session_state["submit"] = False

def write_predict(tags_predict):
    st.write(tags_predict),
    tags_list = tags_predict

def load_model(img):
    json_file = open('/app/streamlit-example/projet5/model_num.json', 'r')

    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("/app/projet5/Formation_ML/model_num.h5")
    #print("Loaded model from disk")

   

tags_suggestion = st.multiselect(
    "Selectionnez des tags:",
    options = tags_list
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
        tags_list = query_title
        write_predict(tags_list)
        st.session_state["submit"] = True

#st_autorefresh(interval=20000, limit=100, key="dataframe")

options = st.multiselect(
    'What are your favorite colors',
    tags_list
    )

st.write('You selected:', options)
