def contagemRegressiva(n):
    if n == 0:
        print("Contagem regressiva finalizada!")
    else:
        print(n)
        contagemRegressiva(n - 1)
contagemRegressiva(10)
