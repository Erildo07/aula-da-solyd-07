import requests 

requisicão =  requests.get('https://solyd.com.br')

print(type(requisicão))
print(requisicão.status_code)