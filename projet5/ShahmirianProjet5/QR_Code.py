import streamlit as st
import pandas as pd
import numpy as np
import os
import time
timestr = time.strftime("%Y%m%d-%H%M%S")

from keras.models import load_model
from keras.applications.vgg16 import preprocess_input, decode_predictions
import pickle

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import contractions
import string
import re
import spacy as sp
import sklearn
import functools


st.set_page_config(page_title="Poser votre question", layout="wide")
init_options = [" "]

def tags_list_change():
    init_options = ["Salut, c'est moi "]#tags_list

#applique la lemmatization et enlève les StopWords, des mots de longeurs 1, et les chiffres """
def lemmatize(text):
	sp.cli.download("en_core_web_sm")
	nlp = sp.load("en_core_web_sm")
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


def load_apply_model(text):

    clean_text = text
    #st.write(text)
    # load model into new model
    pickled_model = pickle.load(open('/app/streamlit-example/projet5/model.pkl', 'rb'))

    x = clean_text(text).split(' ') 
    #preds = pickled_model.predict(x)
    #st.write(str(query_title))
    return x



st.subheader("Poser votre question")

body_text = st.text_area("Détailler votre question)")
title_text = st.text_input("Donner un titre à votre question",autocomplete=" ", on_change=tags_list_change(), key="user_title_text")

submit_button = st.button("Enregistrer")



if "user_title_text" in st.session_state and len(st.session_state.user_title_text) > 0 :
     st.write(title_text)
     if 'options' not in st.session_state:
        st.session_state.options = init_options

     if 'default' not in st.session_state:
        st.session_state.default = []


     ms = st.multiselect(
        label='Pick a number', key="tags_selection",
        options=load_apply_model(title_text),#.split(" "),
        default=st.session_state.default
    )
     
else:
    st.warning("No suggested categories found. Try a different search.")



if submit_button :
	
	st.write("Votre question est enregistrée")

