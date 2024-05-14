import os
import zipfile
import shutil

nome_diretorio = "Textos"
os.makedirs(nome_diretorio)
for i in range(1, 4):
    nome_arquivo = f"arquivo{i}.txt"
    caminho_arquivo = os.path.join(nome_diretorio, nome_arquivo)
    with open(caminho_arquivo, "w") as arquivo:
        arquivo.write("Python Essencial")
shutil.make_archive(nome_diretorio, "zip", nome_diretorio)
print(f"Diretório '{nome_diretorio}' e seus arquivos foram criados e compactados com sucesso.")
