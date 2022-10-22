from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from cleaning import cleaning_tildes,cleaning_html_words 
from prediction_transformation import model_answer_to_front
from pysentimiento import create_analyzer
import time 
import json

hate_speech_analyzer = create_analyzer(task="hate_speech", lang="es")

focus_words = ['comunidad','gay','lgbti','racismo','negros','Mujer','Mujerzuela','incapaz','no inclusivo','desigualdad','genero','orgullo gay','descalificado']
with open('configs/predict_config.json') as json_file:
    predict_dict = json.load(json_file)

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
    response = {
        "texto":[],
        "main_titles":[],
        "second_titles":[]
    }
    data  = info.dict()
    contador = 0
    print('imprimiendo data')
    print(data)
    for llave,valores in data.items():
        if valores != []:
            valores = list(map(cleaning_tildes,valores))
            valores = list(map(cleaning_html_words,valores))
            predicts = hate_speech_analyzer.predict(valores) 
            print(predicts)
            for index,valor in enumerate(valores):
                print('imprimiendo la data limpia *********************')
                print(valor)
                response[llave].append(model_answer_to_front(predict_dict, predicts, index))
                #response[llave].append(sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('mujer'), valor)))
    print('imprimiendo contador') 
    print(contador)
    print('imprimiendo response ')
    print(response)
    time.sleep(2)
    return {"result":response}