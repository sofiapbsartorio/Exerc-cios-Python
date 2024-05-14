import shutil
import os

nome_diretorio = "temp"
if os.path.exists(nome_diretorio):
    shutil.rmtree(nome_diretorio)
    print(f"Diretório '{nome_diretorio}' e todo o seu conteúdo foram excluídos com sucesso.")
else:
    print(f"O diretório '{nome_diretorio}' não existe.")
