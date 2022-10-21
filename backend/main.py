from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
#from cleaning import words_to_delete 
import re
import time
import pysentimiento 


def cleaning_sentences(sentence:str)-> str:
    words_to_delete = ['Δdocument','getElementById', 'ak_js_2',\
    'setAttribute', 'value','new', 'Date', 'getTime','ak_js_3','Debe responder al hcaptcha',\
    'Guarda mi nombre correo electrónico y web en este navegador para la próxima vez que comente',\
    ] 
    sentence = re.sub(r'\W+', ' ', sentence)
    for word in words_to_delete: 
        sentence = sentence.replace(word,'') 
    return sentence 

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
        valores = list(map(cleaning_sentences,valores))
        for valor in valores:
            print('imprimiendo la data limpia *********************')
            print(valor)
            response[llave].append(sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('mujer'), valor)))
    print('imprimiendo contador') 
    print(contador)
    print('imprimiendo response ')
    print(response)
    time.sleep(2)
    return {"result":response}