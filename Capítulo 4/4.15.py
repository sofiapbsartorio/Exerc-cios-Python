frase = input("Digite uma frase: ")
palavras = frase.split()
contagem_palavras = {}
for palavra in palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1
print("Contagem de palavras na frase:")
for palavra, contagem in contagem_palavras.items():
    print(f"A palavra '{palavra}' aparece {contagem} vezes.")
