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
print("Linguagem:", dicionario["Language"])
print("Gênero:", dicionario["Genre"])
print("Tempo de execução:", dicionario["Runtime"])
print("Ano:", dicionario["Year"])
print("Atores:", dicionario["Actors"])
print("Diretor:", dicionario["Director"])
