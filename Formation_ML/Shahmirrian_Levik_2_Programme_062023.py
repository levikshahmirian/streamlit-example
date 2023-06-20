import streamlit as st
#from rembg.bg import remove
from PIL import Image
from io import BytesIO
import base64
import numpy as np
#import joblib
import keras
from keras.models import model_from_json
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, decode_predictions
from keras.utils import img_to_array,load_img

st.set_page_config(layout="wide", page_title="Image Background Remover")

st.write("## Classez des images à l'aide d'algorithmes de Deep Learning")
st.write(
    ":dog:Téléchargez une image de chien pour découvrir sa race. "
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
    col1.write(" ")
    col1.write(" ")
    col1.write(" ")
    col1.image(image)

    #fixed = remove(image)
    #col2.write("la race:wrench:")
    #col2.image(fixed)
    #st.sidebar.markdown("\n")
    #st.sidebar.download_button("Télécharger l'image modiffiée", convert_image(fixed), "fixed.png", "image/png")

def write_predict(prob,imagenet_class_name):
    col2.write("la race:wrench:  "+imagenet_class_name)
    col2.write("la Probabilité   "+ str(prob))
    

#load model, set cache to prevent reloading

def load_model(img):
    json_file = open('/app/streamlit-example/Formation_ML/model_num.json', 'r')

    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)

    # load weights into new model
    loaded_model.load_weights("/app/streamlit-example/Formation_ML/model_num.h5")
    #print("Loaded model from disk")

    x = preprocess_input(np.expand_dims(img.copy(), axis=0))
    preds = loaded_model.predict(x)
    _, imagenet_class_name, prob = decode_predictions(preds, top=1)[0][0]
    write_predict(prob,imagenet_class_name)
   

col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Télécharger une image", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    #fix_image(upload=my_upload)
    img = keras.utils.load_img(my_upload, target_size=(224, 224))
    img = keras.utils.img_to_array(img)
    
    load_model(img)

    fix_image(my_upload)









