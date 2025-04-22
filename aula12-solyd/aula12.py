import requests    #Beautiful soup 4 BS$ pip install bs4

texto = None
try:
    requisicão =  requests.get("https://putsreq.com/6w8pVbaAOHY8aSq2NLec")
    texto = requisicão.text
    print(requisicão.text)
except Exception as e:
    print("Resquisição deu erro: ", e)

print(texto) 

#print(requisicão)
#print(type(requisicão))
#print(requisicão.status_code)