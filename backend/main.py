from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from predict import Prediction
from  data_collect import building_dataframe
#from s3_utils import S3Utils
import boto3
import pandas as pd

predictor = Prediction()
s3 = boto3.client('s3')



class Info(BaseModel):
    """
    Clase que permitra formatear la data que se recibe a través del endpoint.
    """
    texto:List[str]
    main_titles:List[str]
    second_titles:List[str]
    url:str


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Estas intentando entrar al api de escaneo de texto para identificar sesgo, envía una petición POST a la subruta /model."}

@app.post("/model")
def run(info:Info):
    url = info.url
    data  = info.dict()
    df = {
        "textos":[],
        "puntaje":[],
        "url":[]
    }
    del data["url"]
    for key in data:
        for text in key:
            df["textos"].append(text)


    response = predictor.infer(info=data) 
    print('imprimiendo response ')
    response["url"] = url
    for p in response:
        for punt in p:
            df["puntaje"].append(punt)
            df["url"].append(url)
    #building_dataframe(response, s3)
    print(df)

    return {"result":response}

