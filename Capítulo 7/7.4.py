import os

nome_arquivo = input("Digite o nome do arquivo: ")
if os.path.exists(nome_arquivo):
    nome, extensao = os.path.splitext(nome_arquivo)
    novo_nome_arquivo = nome + "_renomeado" + extensao
    os.rename(nome_arquivo, novo_nome_arquivo)
    print(f"Arquivo renomeado para '{novo_nome_arquivo}' com sucesso.")
else:
    print("O arquivo não existe.")
