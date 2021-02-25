from fastapi import FastAPI
from fastapi import UploadFile , File
import uvicorn
from fastapi.encoders import jsonable_encoder
from prediction import *
from pydantic import BaseModel


class Item(BaseModel):
    image: str


app = FastAPI()

@app.get('/index')
def hello_word():
    return 'hi yo'

# @app.post('/api/predict')
# def predict_image(file: bytes = File(...)):
#     # read the file upload by user
#     image = read_image(file)
#     # preprocessing
#     image = preprocess(image)
#     # predict
#     predictions = predict(image)
#
#
#     return {"prediction": predictions}

@app.post('/api/predict')
async def predict_image(item:Item):
        image = decod(item.image)
        # # preprocessing
        image = preprocess(image)
        # # predict
        predictions = predict(image)
        # print(predictions)
        return predictions
        # print(item.image)


    # return {"image" : image}







if __name__ == '__main__':
    uvicorn.run(app,port=8080,host='0.0.0.0')
