numeros = input("Digite uma lista de números separados por espaço: ").split()
quadrados = list(map(lambda x: int(x) ** 2, numeros))
print("Quadrados dos números:", quadrados)
