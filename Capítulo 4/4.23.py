from datetime import datetime

data_jan = datetime(2022, 1, 1)
data_fev = datetime(2022, 2, 1)
diferenca_dias = (data_fev - data_jan).days
print("Diferença entre 1 de janeiro e 1 de fevereiro de 2022 em dias:", diferenca_dias)
