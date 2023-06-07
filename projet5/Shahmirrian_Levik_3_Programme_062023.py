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

nlp = sp.load("en_core_web_sm")

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

    # load model into new model
    pickled_model = pickle.load(open('model.pkl', 'rb'))

    x = preprocess_input(np.expand_dims(img.copy(), axis=0))
    preds = pickled_model.predict(x)


"""Développer les contractions"""
def Expand_the_Contractions(text):
    return contractions.fix(text)

"""applique la lemmatization et enlève les StopWords, des mots de longeurs 1, et les chiffres """
def lemmatize(text):
   doc = nlp(text)
   tokens = [token.lemma_ for token in doc if not (token.is_stop or token.is_punct or len(token) == 1 or token.is_digit)]
   return ' '.join(tokens)


""" Imprimer la chaîne après avoir supprimé les balises"""
def RemoveHTMLTags(text):
    return re.compile(r'<[^>]+>').sub('', text)

"""supprimer les interligne"""
def remove_line_breaks(text):
    text = text.replace('\r', ' ').replace('\n', ' ')
    return text

"""supprimer la ponctuation"""
def remove_punctuation(text):
    re_replacements = re.compile("__[A-Z]+__")  # such as __NAME__, __LINK__
    re_punctuation = re.compile("[%s]" % re.escape(string.punctuation))
    '''Échappez tous les caractères du modèle sauf les lettres et les chiffres ASCII'''
    tokens = word_tokenize(text.lower())
    tokens_zero_punctuation = []
    for token in tokens:
        if not re_replacements.match(token):
            token = re_punctuation.sub(" ", token)
        tokens_zero_punctuation.append(token)
    return ' '.join(tokens_zero_punctuation)

def lowercase(text):
    #text_low = [token.lower() for token in word_tokenize(text)]
    text_low= word_tokenize(text.lower())
    return text_low

# removing stopwords
def remove_stopwords(text):
    words = [w for w in text if w not in stopwords.words('english')]
    return words 

def clean_text(text):
    _steps = [
    RemoveHTMLTags,
    remove_line_breaks,
    Expand_the_Contractions,
    remove_punctuation,
    remove_stopwords,
    lemmatize

    ]
    for step in _steps:
        text=step(text)
    return text   

    

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
