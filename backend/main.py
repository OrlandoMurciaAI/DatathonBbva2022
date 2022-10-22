from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from predict import Prediction
import time 
import json


focus_words = ['comunidad','gay','lgbti','racismo','negros','Mujer','Mujerzuela','incapaz','no inclusivo','desigualdad','genero','orgullo gay','descalificado']


predictor = Prediction()


class Info(BaseModel):
    texto:List[str]
    main_titles:List[str]
    second_titles:List[str]


app = FastAPI()
# origins = [
#     "http://localhost.tiangolo.com",
#     "https://localhost.tiangolo.com",
#     "http://localhost",
#     "http://localhost:8080",
# ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/model")
def run(info:Info):
    response = predictor.infer(info=info) 
    print('imprimiendo response ')
    print(response)
    time.sleep(2)
    return {"result":response}