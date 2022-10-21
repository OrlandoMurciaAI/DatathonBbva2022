from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import re
import time

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
    print(data)
    for i,j in data.items():
        for p in j:
            response[i].append(sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('mujer'), p)))
    print(contador)
    print(response)
    time.sleep(2)
    return {"result":response}