import random
import string

class InputInvalidoException(Exception):
    pass

def obter_palavra_secreta():
    palavras = ["sofia"]
    return random.choice(palavras)

def adivinhacao_palavra():
    palavra_secreta = obter_palavra_secreta()
    letras_certas = set()
    letras_erradas = set()
    while True:
        palavra_atual = ''.join(letra if letra in letras_certas else '_' for letra in palavra_secreta)
        print("Palavra secreta:", palavra_atual)
        
        try:
            letra = input("Digite uma letra: ").lower()
            
            if len(letra) != 1 or letra not in string.ascii_lowercase:
                raise InputInvalidoException("Por favor, digite apenas uma letra do alfabeto.")
            
            if letra in palavra_secreta:
                letras_certas.add(letra)
                if letras_certas == set(palavra_secreta):
                    print("Parabéns! Você acertou a palavra:", palavra_secreta)
                    break
        
        except InputInvalidoException as e:
            print(e)

adivinhacao_palavra()
