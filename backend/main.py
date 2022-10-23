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

def create_dict(base):
    lista = []
    for p in base:
        for punt in base[p]:
            lista.append(punt)
    return lista



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
        for text in data[key]:
            df["textos"].append(text)
    df["textos"] = create_dict(data)
    
    response = predictor.infer(info=data) 
    df["puntaje"] = create_dict(response)
    print('imprimiendo response ')
    response["url"] = url
    df['url'] = [url for _ in df["textos"] ]
    building_dataframe(df, s3)


    return {"result":response}



