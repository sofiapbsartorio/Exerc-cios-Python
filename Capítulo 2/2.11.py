idade = int(input("Digite sua idade: "))
nacionalidade = input("Digite sua nacionalidade: ")
if idade >= 16 and nacionalidade.lower() == "brasileiro":
    print("Você pode votar.")
else:
    print("Você não pode votar.")
