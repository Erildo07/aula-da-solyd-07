import re
import requests

requests = requests.get("https://descubraatibaia.tur.br/sem-categoria/contato/")

#string_de_test = "o gato,a gata, os gatinhos, os gatões é bonito"

padrão = re.findall(r"[\w\.-]+@[\w-]+\.[\w\.-]+", requests.text)


if  padrão:
    print(padrão)
    
else:
    print("Padrão não encontrado")

print