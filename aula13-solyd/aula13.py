import requests

# Inclua a chave de API diretamente na URL
req = requests.get('http://www.omdbapi.com/?t=Harry+potter&apikey=3b28a7e')

# Exiba o conteúdo da resposta
print(req.text)
