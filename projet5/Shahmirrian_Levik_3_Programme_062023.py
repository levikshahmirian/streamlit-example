import streamlit as st
import pandas as pd
import numpy as np

import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import contractions
import string

import spacy as sp
import sklearn
import functools

import base64
import io
import zipfile
import filetype

st.set_page_config(page_title="Poser votre question",)
init_options = [" "]

st.sidebar.write("## Charger le modèle :gear:")
my_upload = st.sidebar.file_uploader("Télécharger une image", type=["pickle", "pkl", "zip"])

if my_upload is not None:
    #fix_image(upload=my_upload)
	
	st.sidebar.write("Ca Marché")


#applique la lemmatization et enlève les StopWords, des mots de longeurs 1, et les chiffres """
def lemmatize(text):
	sp.cli.download("en_core_web_sm")
	nlp = sp.load("en_core_web_sm")
	doc = nlp(text)
	tokens = [token.lemma_ for token in doc if not (token.is_stop or token.is_punct or len(token) == 1 or token.is_digit or token.like_url)]
	return ' '.join(tokens)

def removeSpecialChar(text):
    char_remov = ['"', '(', ')', "'", '[', ']']
    for char in char_remov:
        # replace() "returns" an altered string
        clean_text = text.replace(char, " ")
    return str(clean_text)


def clean_text(text):
    _steps = [
    removeSpecialChar,
    #Expand_the_Contractions,
    lemmatize
    ]
    for step in _steps:
        text=step(text)
    return text   

def load_apply_model(text):
    #st.write(text)
    # load model into new model

    pickled_model = pickle.load(open('projet5/model.pkl', 'rb'))
    pickled_vectorizer = pickle.load(open('projet5/vectorizer.pickle', 'rb'))
    
    corpora_Lemm_Title = clean_text(text).split()
    x = pickled_vectorizer.transform(corpora_Lemm_Title)
    feature_names_Title = pickled_vectorizer.get_feature_names_out()

    #sorted_items=sort_coo(tf_idf_vector.tocoo())
    
    #x = clean_text(text).split()
    preds = pickled_model.predict(x)

    

    st.write(preds.tolist())
    return feature_names_Title


st.subheader("Poser votre question")

body_text = st.text_area("Détailler votre question)")
title_text = st.text_input("Donner un titre à votre question",autocomplete=" ", key="user_title_text")

if "user_title_text" in st.session_state and len(st.session_state.user_title_text) > 0 :
     #st.write(title_text)
     if 'options' not in st.session_state:
        st.session_state.options = init_options

     if 'default' not in st.session_state:
        st.session_state.default = []

     ms = st.multiselect(
        label='Pick a number', key="tags_selection",
        options=load_apply_model(title_text),
        default=st.session_state.default
    )    
else:
    st.warning("Saisissez votre question et valider pour obtenir des tags.")

submit_button = st.button("Enregistrer")
if submit_button :
	st.write("Votre question est enregistrée")
