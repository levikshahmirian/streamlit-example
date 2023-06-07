import streamlit as st
import pandas as pd
import requests
import json
import numpy as np 
from keras.models import model_from_json
from keras.models import load_model
from keras.applications.vgg16 import preprocess_input, decode_predictions
import pickle

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import contractions
import string
import re
import spacy as sp



st.set_page_config(page_title="Poser votre question", layout="wide")
st.sidebar.header("Choisissez les tags:")
init_options = [""]
tags_list = [""]

sp.cli.download("en_core_web_sm")
nlp = sp.load("en_core_web_sm")

# ---- MAINPAGE ----
st.title("Formation_ML Projet 5 ")
st.markdown("##")


#applique la lemmatization et enlève les StopWords, des mots de longeurs 1, et les chiffres """
def lemmatize(text):
   
   doc = nlp(text)
   tokens = [token.lemma_ for token in doc if not (token.is_stop or token.is_punct or len(token) == 1 or token.is_digit or token.like_url)]
   
   return ' '.join(tokens)


def RemoveHTMLTags(text):
    tag = False
    quote = False
    out = ""

    for c in text:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c

    return out

def lowercase(text):

    return text.lower()

def clean_text(text):
    _steps = [
    RemoveHTMLTags,
    lowercase,
    #Expand_the_Contractions,
    lemmatize
    ]
    for step in _steps:
        text=step(text)
    return text   


def load_apply_model(clean_text):

    # load model into new model
    pickled_model = pickle.load(open('model.pkl', 'rb'))

    x = clean_text(query_title).split(' ') 
    preds = pickled_model.predict(x)

query_body = st.text_area("Ask a question about the document")
query_title = st.text_input(label="Topic (or hashtag)", placeholder="Title", on_change= load_apply_model(query_title))
#Développer les contractions"""
#def Expand_the_Contractions(text):
    #return contractions.fix(text)



    

#query_title = query_title
#st.session_state.options = clean_text(query_title).split(' ') 

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
