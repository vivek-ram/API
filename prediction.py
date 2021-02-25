from PIL import Image
from io import BytesIO
import tensorflow as tf
import numpy as np
import base64
import io


input_shape = (224,224)

def load_model():
    model = tf.keras.models.load_model("model_V1.h5")
    return model

model = load_model()

def decod(b64):
    image = base64.b64decode(str(b64))
    img = Image.open(io.BytesIO(image))
    return img



def preprocess(image : Image.Image):

    image = image.resize(input_shape)
    image = np.asfarray(image)
    image = image / 127.5 - 1.0
    image = np.expand_dims(image,0)
    return image


def predict(image: np.ndarray):
    label = {'akiec': 0, 'bcc': 1, 'bkl': 2, 'df': 3, 'mel': 4, 'melanoma': 5, 'nevus': 6, 'nv': 7, 'seborrheic_keratosis': 8, 'vasc': 9}
    classes = list(label)
    predictions = classes[np.argmax(model.predict(image))]
    return predictions
