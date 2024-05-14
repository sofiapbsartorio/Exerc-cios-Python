class SaldoInsuficienteException(Exception):
    pass

class ContaBancaria:
    def __init__(self, saldo_inicial=0):
        self.saldo = saldo_inicial

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteException("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor
        print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

conta = ContaBancaria(1000)

try:
    conta.sacar(1500)
except SaldoInsuficienteException as e:
    print(e)

conta.depositar(500)
conta.sacar(1500)
