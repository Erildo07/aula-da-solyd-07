import re   

string_de_test = "o gato,a gata, os gatinhos, os gatões é bonito"

padrão = re.findall(r"[gat]",string_de_test)


if  padrão:
    print(padrão)
    
else:
    print("Padrão não encontrado")