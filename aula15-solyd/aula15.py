import requests
import json

# Solicita cotação de dólar, euro e bitcoin
url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
resposta = requests.get(url)

cotação = json.loads(resposta.text)

# Mostra as cotações
print("### COTAÇÃO ###")
print("Dólar:", cotação['USDBRL']['bid'])
print("Euro:", cotação['EURBRL']['bid'])
print("Bitcoin:", cotação['BTCBRL']['bid'])
