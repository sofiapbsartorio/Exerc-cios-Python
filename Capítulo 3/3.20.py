n = int(input("Digite um número para calcular o fatorial de todos os números de 1 a n: "))
for i in range(1, n + 1):
    fatorial = 1
    for j in range(1, i + 1):
        fatorial *= j
    print(f"O fatorial de {i} é: {fatorial}")
