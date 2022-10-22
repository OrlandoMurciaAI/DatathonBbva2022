from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
#from cleaning import words_to_delete 
import re
import time
from pysentimiento import create_analyzer
import json 
hate_speech_analyzer = create_analyzer(task="hate_speech", lang="es")

focus_words = ['comunidad','gay','lgbti','racismo','negros','Mujer','Mujerzuela','incapaz','no inclusivo','desigualdad','genero','orgullo gay','descalificado']

with open('configs/predict_config.json') as json_file:
    predict_dict = json.load(json_file)

def cleaning_tildes(sentence: str)->str: 
    """
    Definition: replace the tildes found in the sentence
    """
    sentence = sentence.replace('á','a').replace('é','e').replace('í','i').replace('ó','o').replace('ú','u') 

    return sentence 

def cleaning_html_words(sentence:str)-> str:
    """
    Definition: Delete any html/js/css tag found at the moment of scrapping the data. 
                Also deletes not alphanumeric chars found in the sentence
    input: the sentence we are trying to clean 
    output: the sentence cleaned
    """
     
    words_to_delete = ['Δdocument','getelementbyid', 'ak_js_2',\
    'setattribute', 'value','new', 'Date', 'getTime','ak_js_3','Debe responder al hcaptcha',\
    'Guarda mi nombre correo electrónico y web en este navegador para la próxima vez que comente',\
    ] 
    sentence = re.sub(r'\W+', ' ', sentence)
    for word in words_to_delete: 
        sentence = sentence.replace(word,'') 
    return sentence 

def model_answer_to_front(predict_dict: dict, predicts,index: int)-> str: 
    print('*************ENTRANDO AL MODELO**************')
    prediction = predicts[index].output
    print(prediction)
    if prediction == []:
        prediction_result = '#FFFFFF'
        return prediction_result
    prediction.sort() 
    key_value = ','.join(prediction)
    prediction_result = predict_dict[key_value]
    return prediction_result 

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