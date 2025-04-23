import requests
import json
req = None

try:
    req = requests.get('http://www.omdbapi.com/?t=Harry+potter&apikey=3b28a7e')
except:
    print("Erro na conexão")
    exit()

dicionario = json.loads(req.text)

print(dicionario["Title"])