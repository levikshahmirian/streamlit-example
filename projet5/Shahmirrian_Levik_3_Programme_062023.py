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

# ---- MAINPAGE ----
st.title("Formation_ML Projet 5 ")
st.markdown("##")

def tags_list_change():
    init_options = tags_list


query_body = st.text_area("Ask a question about the document")
query_title = st.text_input(label="Topic (or hashtag)", placeholder="Title", on_change= tags_list_change())

def load_apply_model(img):

    # load model into new model
    pickled_model = pickle.load(open('model.pkl', 'rb'))

    x = preprocess_input(np.expand_dims(img.copy(), axis=0))
    preds = pickled_model.predict(x)


#Développer les contractions"""
def Expand_the_Contractions(text):
    return contractions.fix(text)

#applique la lemmatization et enlève les StopWords, des mots de longeurs 1, et les chiffres """
def lemmatize(text):
   nlp = sp.load("en_core_web_sm")
   doc = nlp(text)
   tokens = [token.lemma_ for token in doc if not (token.is_stop or token.is_punct or len(token) == 1 or token.is_digit)]
   return ' '.join(tokens)

def preprocess_text(text):
    #Make text lowercase, remove text in square brackets,remove links,remove punctuation
    #and remove words containing numbers.'''
    text = [each_string.lower() for each_string in text]
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    return text

#supprimer les interligne"""
def remove_line_breaks(text):
    text = text.replace('\r', ' ').replace('\n', ' ')
    return text

# removing stopwords
def remove_stopwords(text):
    words = [w for w in text if w not in stopwords.words('english')]
    return words 

def clean_text(text):
    _steps = [
    preprocess_text,
    remove_line_breaks,
    Expand_the_Contractions,
    remove_stopwords,
    lemmatize
    ]
    for step in _steps:
        text=step(text)
    return text   

    

query_title = query_title.split(' ') 
st.session_state.options = clean_text(query_title)

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
