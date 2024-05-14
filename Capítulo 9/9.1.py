def dividir_numeros():
    try:
        num1 = int(input("Digite o primeiro número inteiro: "))
        num2 = int(input("Digite o segundo número inteiro: "))
        
        if num2 == 0:
            raise ZeroDivisionError("Não é possível dividir por zero.")
        
        resultado = num1 / num2
        print("O resultado da divisão é:", resultado)
    
    except ValueError:
        print("Por favor, digite apenas números inteiros.")
    except ZeroDivisionError as e:
        print("Erro:", e)

dividir_numeros()
