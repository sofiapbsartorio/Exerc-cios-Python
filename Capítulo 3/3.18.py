n = int(input("Digite o número de termos da sequência de Fibonacci: "))
fibonacci = [0, 1]
for i in range(2, n):
    proximo_termo = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_termo)
print("Sequência de Fibonacci até o", n, "-ésimo termo:")
for termo in fibonacci:
    print(termo, end=" ")
