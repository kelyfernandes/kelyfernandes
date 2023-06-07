@@ -13,28 +13,17 @@
    allow_headers=["*"],
)

def ler_arquivo():  

def ler_arquivo():    
    with open('registros.json', 'r') as dados:
        try:
            return list(json.load(dados))
            return  list(json.load(dados))
        except:
            return []

@app.get("/")
def ola_mundo():
    return "Ola Mundo"







@app.get("/")
@app.get("/api/registros")
def listar_registros():



    registros = ler_arquivo()

    if not registros:
 2 changes: 1 addition & 1 deletion2  
front/script.js
@@ -1,4 +1,4 @@
const apiUrl = 'http://192.168.0.36:8000/api/registros';
const apiUrl = 'http://localhost:8000/api/registros';

function enviar() {
  const nome = document.getElementById("nome").value;
