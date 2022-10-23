from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from predict import Prediction

predictor = Prediction()


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
    del info.url
    response = predictor.infer(info=info) 
    print('imprimiendo response ')
    response.url = url
    building_dataframe(response)

    return {"result":response}