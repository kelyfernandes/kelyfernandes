from funcao import calcular_idade
import json

arquivo = open("arquivo.json", "r")  # r = read = ler

lista = list(json.load(arquivo))


def ler_arquivo():
    texto = ""
    
    for dicionario in lista:
        nome = dicionario["nome"]
        nascimento = dicionario["nascimento"]

        if nome.lower() == "zero" or nome == "0":
            print("nome invalido")
            continue
        
        idade = calcular_idade(nascimento)
        
        if idade == -1:
            print('invalida')
            continue
        
        texto += f"seu nome é {nome}, sua idade é {idade}; "

    return texto
        

ler_arquivo()

lista.append({
        "nome": "ZEROOOO",
        "nascimento": "30/11/1981"
    })

arquivo2 = open("arquivo2.json", "w")  # w = write = escrever
arquivo2.write(json.dumps(lista, indent=4))
