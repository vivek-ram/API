from fastapi import FastAPI
from fastapi import UploadFile , File
import uvicorn
from fastapi.encoders import jsonable_encoder
from prediction import *
from pydantic import BaseModel


class Item(BaseModel):
    image: str


app = FastAPI()


@app.post('/')
async def predict_image(item:Item):
        image = decod(item.image)
        image = preprocess(image)
        predictions = predict(image)
        return predictions
