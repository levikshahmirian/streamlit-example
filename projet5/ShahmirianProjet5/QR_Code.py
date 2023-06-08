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



def tags_list_change():
    init_options = [" "]#tags_list

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


def load_apply_model(clean_text):

    # load model into new model
    pickled_model = pickle.load(open('/app/streamlit-example/projet5/model.pkl', 'rb'))

    #x = clean_text(query_title).split(' ') 
    #preds = pickled_model.predict(x)
    #st.write(str(query_title))



st.subheader("Poser votre question")
with st.form(key='myqr_form'):
	body_text = st.text_area("Détailler votre question)")

	title_text = st.text_area("Donner un titre à votre question", on_change= tags_list_change())
	submit_button = st.form_submit_button("Enregistrer")
	


if submit_button :
	col1, col2 = st.columns(2)
	with col1:


		# Filename
		img_filename = "{}.png".format(title_text)
		path_for_images = os.path.join(img_filename)


	with col2:
		st.info('Nama Toko')
		st.write("df4")


