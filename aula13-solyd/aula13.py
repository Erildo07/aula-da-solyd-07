import requests

req = None

try:
    req = requests.get('http://www.omdbapi.com/?t=Harry+potter&apikey=3b28a7es')
except:
    print("Erro na conexão")
    exit()

print(req.text)
