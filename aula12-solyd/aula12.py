import requests    #Beautiful soup 4 BS$ pip install bs4

cabecalho = {"user-agent ": "windows ", 
             "Referer": "https:// google.com",
             "cf-ipcountry": "US"}

meus_cookies = {"ultima visita": "21-04-2025" }

dados = {"usarname": "Eridlo",
        "password": "123"}

texto = None
try:
    #requisicão =  requests.get("https://putsreq.com/b1Gv9Fy4IAZgp3a8qc1I")
    requisicão =  requests.post("https://putsreq.com/b1Gv9Fy4IAZgp3a8qc1I",
                                headers=cabecalho,
                                cookies=meus_cookies,
                                data=dados)
    texto = requisicão.text
    #print(requisicão.text)
except Exception as e:
    print("Resquisição deu erro: ", e)

print(texto) 

#print(requisicão)
#print(type(requisicão))
#print(requisicão.status_code)