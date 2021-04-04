from PIL import Image
from io import BytesIO
import tensorflow as tf
import numpy as np
import base64
import io


input_shape = (224,224)

def load_model():
    model = tf.keras.models.load_model("vgg16_B1.h5")
    return model

model = load_model()

def decod(b64):
    image = base64.b64decode(str(b64))
    img = Image.open(io.BytesIO(image))
    return img



def preprocess(image : Image.Image):

    image = image.resize(input_shape)
    image = np.asfarray(image)
    image = image / 225
    image = np.expand_dims(image,0)
    return image


def predict(image: np.ndarray):
    label = {'Bowen’s disease': 0, 'Basal cell carinoma': 1, 'benign keratosis': 2, 'dermatofibroma': 3, 'melanoma': 4, 'melanocytic nevi': 5, 'vascular lesions': 6}
    classes = list(label)
    predictions = classes[np.argmax(model.predict(image))]
    prob = model.predict(image)
    temp = ['Bowen’s disease','Basal cell carinoma','benign keratosis','dermatofibroma','melanoma','melanocytic nevi','vascular lesions']
    dum = 0
    for i in temp:
        label[i] = str(round(prob[0][dum]*100,2)) + '%'
        dum += 1
    dic = {'prediction':predictions,'probability':label}
    return dic


