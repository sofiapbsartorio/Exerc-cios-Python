import os

nome_arquivo = input("Digite o nome do arquivo: ")
try:
    with open(nome_arquivo, "r") as arquivo:
        conteudo = arquivo.read()
    print("Conteúdo do arquivo:")
    print(conteudo)
except FileNotFoundError:
    print("Arquivo não encontrado.")
except:
    print("Ocorreu um erro ao ler o arquivo.")
