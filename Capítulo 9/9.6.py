import random

class InputInvalidoException(Exception):
    pass

def jogo_adivinhacao():
    numero_secreto = random.randint(1, 10)
    while True:
        try:
            palpite = int(input("Digite um número entre 1 e 10: "))
            
            if palpite < 1 or palpite > 10:
                raise InputInvalidoException("Número fora do intervalo permitido.")
            
            if palpite == numero_secreto:
                print("Parabéns! Você acertou o número secreto!")
                break
            else:
                print("Ops! Tente novamente.")
        except ValueError:
            print("Por favor, insira apenas números inteiros.")
        except InputInvalidoException as e:
            print(e)
jogo_adivinhacao()
