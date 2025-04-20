import time

def abre_arquivo():
    try:

        arquivo = open("arquivo07.txt")
        return True
    except Exception as erro:
        print("Aconteceu  algun erro: ", erro)
        return False
    
while not abre_arquivo():
    print("tentando abrir o arquivo")
    time.sleep(7)
print("consguiu abri arquivo: ")

#print("AAa")
#try:
#    a = 120 / 0 
#except:
#    print("Divisão por 0, não da pra fazer: ")