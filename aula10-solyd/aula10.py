#arquivo = open("/home/kali/Downloads/𝐭𝐨𝐝𝐨𝐫𝐨𝐤𝐢 𝐬𝐡𝐨𝐮𝐭𝐨 _ 𝐛𝐨𝐤𝐮 𝐧𝐨 𝐡𝐞𝐫𝐨 𝐚𝐜𝐚𝐝𝐞𝐦𝐢𝐚.jpeg", "rb")
arquivo = open("arquivo.txt", "w")
# cria o arquivo txt rescreve
arquivo.write("Fala comigo !!")
# escreve na pasta aruivo.txt
type(print(arquivo))
for i in range(0, 100):
    arquivo.write("aa: "+str(i)+"\n")
#print(arquivo)
# "r" le o arquivo e printa  na terminal 
#print(arquivo.read())

#for linha in arquivo:
#    print(linha)