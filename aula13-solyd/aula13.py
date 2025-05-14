import requests
import json
req = None

def requisição(titulo):
    try:
        req = requests.get(f'http://www.omdbapi.com/?t={titulo}&apikey=3b28a7e')
        dicionario = json.loads(req.text)
        return dicionario, req.url  
    except:
        print("Erro na conexão")
        return None

def printar_detahes(filme):

    print("Titulo:", filme["Title"])
    print("Avaliação imdb:", filme["imdbRating"])
    print("Linguagem:", filme["Language"])
    print("Gênero:", filme["Genre"])
    print("Tempo de execução:", filme["Runtime"])
    print("Ano:", filme["Year"])
    print("Atores:", filme["Actors"])
    print("Trofeus:", filme["Awards"])
    print("Diretor:", filme["Director"])
    print("Poster:", filme["Poster"])
    print("")

sair = False
while not sair:
    print("")
    print("         ------************--------")
    print("")
    op = input("Escreva o nome de um filme ou Sair para fechar: ")
    print("")

    if op.upper() == "SAIR":
        sair = True
        print("Saindo .....")
    else:
        filme, url = requisição(op)
        if filme is None or filme.get("Response") == "False":
            print("Filme não encontrado")
        else:
            printar_detahes(filme)
            print("URL gerada:", url)
