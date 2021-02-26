# import tensorflow as tf
# import cv2
# import numpy as np
# path = '/Users/vivekd/Downloads/Skin Cancer Prediction /DataSet/Val/bcc/ISIC_0024332.jpg'
#
# model = tf.keras.models.load_model("vgg16_V4.h5")
#
# label = {'akiec': 0, 'bcc': 1, 'bkl': 2, 'df': 3, 'mel': 4, 'melanoma': 5, 'nevus': 6, 'nv': 7, 'seborrheic_keratosis': 8, 'vasc': 9}
# classes = list(label)
#
# x = cv2.imread(path)
# x = x/255.
# x = np.resize(x,(1,224,224,3))
# print(classes[np.argmax(model.predict(x))])
#
#
# def predict(image : Image.Image):
#     label = {'akiec': 0, 'bcc': 1, 'bkl': 2, 'df': 3, 'mel': 4, 'melanoma': 5, 'nevus': 6, 'nv': 7, 'seborrheic_keratosis': 8, 'vasc': 9}
#     classes = list(label)
#     x = cv2.imread(image)
#     x = x/255.
#     x = np.resize(x,(1,224,224,3))
#     prediction = classes[np.argmax(model.predict(x))]
#     return prediction
import requests
# from fastapi.testclient import TestClient


filename = '/Users/vivekd/Downloads/Skin Cancer Prediction /Test/seborrheic_keratosis/ISIC_0012199.jpg'


import requests

url = "https://fastapi-skincancer.herokuapp.com"

# r = requests.post(url, files={"file": ("filename", open(filename, 'rb'))})
# # assert r.status_code == 200
# # print(r.content)
#
# print(r.json())

r =  requests.post(url,{image : "hi"})


























# files = {"file": ('/Users/vivekd/Downloads/Skin Cancer Prediction /DataSet/Val/mel/ISIC_0024315.jpg', "multipart/form-data")}
# response = requests.post('http://0.0.0.0:8080/api/predict', files = files )
#
#
# # print(a.content)
# # print(response.content)
#
# print(response.status_code)
# print(response.text)
