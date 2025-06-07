import re   

string_de_test = "o gato é bonito"

padrão = re.search("",string_de_test)

print(padrão.group("ola"))