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
