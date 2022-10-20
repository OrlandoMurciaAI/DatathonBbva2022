from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import re
import time

class Info(BaseModel):
    textos:List[str]
    titulos:List[str]
    titulos_sec:List[str]


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
    data  = info.dict()
    contador = 0
    for p in data["textos"]:
        contador += sum(1 for _ in re.finditer(r'\b%s\b' % re.escape('mujer'), p))
    print(contador)
    print(info)
    time.sleep(2)
    return {"result":contador}