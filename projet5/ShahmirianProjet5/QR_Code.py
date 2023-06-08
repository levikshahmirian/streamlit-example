import streamlit as st
import pandas as pd
from PIL import Image
import numpy as np
import os
import time
timestr = time.strftime("%Y%m%d-%H%M%S")




def load_image(img):
	im = Image.open(img)
	return im

st.subheader("Create QR Code")
with st.form(key='myqr_form'):
	raw_text = st.text_area("Input Kode Outlet disini (Kode Huruf Menggunakan Huruf Kapital)", max_chars=8)
	submit_button = st.form_submit_button("Generate")
	df = pd.read_excel(
    		io ="List_QR.xlsx",
    		engine="openpyxl",
    		sheet_name="Customer",
    		usecols="B:H",
    		nrows=20000,
    		) 

	#df1 = df.drop(['Nama_Outlet','Alamat','Zona','Sektor','Tgl Process'], axis=1)
	df1 = df.drop(['Alamat','Zona','Sektor','Tgl Process'], axis=1)


	df2 = df1[df1["OutletID"].str.contains(raw_text)]
	#df4 = df2.iloc[0][1]
	df3 = df2.iloc[0][2]
	df4 = df2.iloc[0][1]

	
	#st.write(df3)

if submit_button :
	col1, col2 = st.columns(2)
	with col1:


		# Filename
		img_filename = "{}.png".format(raw_text)
		path_for_images = os.path.join(img_filename)
		

		final_img = load_image(path_for_images)
		st.image(final_img)

	with col2:
		st.info('Nama Toko')
		st.write(df4)


