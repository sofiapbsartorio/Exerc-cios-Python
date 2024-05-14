class ContaBancaria:
    def __init__(self):
        self.saldo = 0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente ou valor inválido para saque.")

    def exibir_saldo(self):
        print(f"Saldo atual: R${self.saldo:.2f}")
conta = ContaBancaria()
conta.exibir_saldo()  
conta.depositar(100)
conta.exibir_saldo()  
conta.sacar(50)
conta.exibir_saldo()  
conta.sacar(100)  
