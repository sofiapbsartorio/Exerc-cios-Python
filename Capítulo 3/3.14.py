numero = int(input("Digite um número para verificar se é primo: "))
primo = True
if numero <= 1:
    primo = False
else:
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            primo = False
            break
if primo:
    print(numero, "é primo.")
else:
    print(numero, "não é primo.")
