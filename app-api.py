import json

from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins="*",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def ola_mundo():
    return "Olá Mundo"


from datetime import datetime, date
from funcao_nascimento import calcular_idade 

hoje = date.today()

def ler_de_funcao_nascimento():
    arquivo = open("arquivo.json", "r")
    lista = list(json.load(arquivo))
    texto = ""
    
    dicionario = json.load(arquivo)
    
    for i in dicionario:
        nome =  i['nome']

        if nome.lower() == "zero" or nome == "0":
            continue

        nascimento = i['nascimento']

        idade = calcular_idade(nascimento)
        
        if idade < 0:
            continue
    
    return texto

    
