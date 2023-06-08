import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import os
import time
timestr = time.strftime("%Y%m%d-%H%M%S")


st.subheader("Poser votre question")
with st.form(key='myqr_form'):
	body_text = st.text_area("Détailler votre question)")

	title_text = st.text_area("Donner un titre à votre question")
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


