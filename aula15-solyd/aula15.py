import requests
import json
import time
import datetime


    # Solicita cotação de dólar, euro e bitcoin
while True:

    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL"
    resposta = requests.get(url)

    cotação = json.loads(resposta.text)

    # Mostra as cotações
    print("### COTAÇÃO ###  ", datetime.datetime.now())
    print("Dólar:", cotação['USDBRL']['bid'])
    print("Euro:", cotação['EURBRL']['bid'])
    print("Bitcoin:", cotação['BTCBRL']['bid'])
    print("")
    print("************")
    print("")
    time.sleep(5)
    
