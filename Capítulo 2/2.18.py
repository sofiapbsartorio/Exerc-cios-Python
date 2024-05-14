numeros = []
for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(numero)
todos_pares = all(numero % 2 == 0 for numero in numeros)
if todos_pares:
    print("Todos os números digitados são pares.")
else:
    print("Pelo menos um dos números digitados é ímpar.")
