import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64
import numpy
import joblib

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Classez des images à l'aide d'algorithmes de Deep Learning")
st.write(
    ":dog:Téléchargez une image de chien pour découvrir sa race. Des images de qualité complète peuvent être téléchargées à partir de la barre latérale. Special thanks to the [rembg library](https://github.com/danielgatis/rembg) :grin:"
)
st.sidebar.write("## Charger et télécharger :gear:")
# Download the fixed image
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Image Originale:camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("la race:wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Télécharger l'image modiffiée", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Télécharger une image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    fix_image(upload=my_upload)
else:
    fix_image("/app/streamlit-example/BackgroundRemoval-main/zebra.jpg")


col1, col2 = st.columns(2)
my_upload1 = st.sidebar.file_uploader("Télécharger une Model", type=["pkl"])

if my_upload1 is not None:
    #load saved model
    xgb = joblib.load(my_upload1)
    




