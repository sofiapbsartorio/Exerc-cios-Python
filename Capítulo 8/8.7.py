class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def mostrar_dados(self):
        super().mostrar_dados()
        print(f"Salário: R${self.salario:.2f}")

lista_pessoas_funcionarios = [
    Pessoa("João", 30),
    Pessoa("Maria", 25),
    Funcionario("Pedro", 35, 2500.00),
    Funcionario("Ana", 28, 3000.00)
]

for pessoa_funcionario in lista_pessoas_funcionarios:
    pessoa_funcionario.mostrar_dados()
    print("\n")