class Carro:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self, segundos):
        aceleracao = 10  # m/s^2
        self.velocidade += aceleracao * segundos
        print(f"O carro acelerou e atingiu a velocidade de {self.velocidade} m/s.")

    def frear(self, segundos):
        desaceleracao = 5  # m/s^2
        self.velocidade -= desaceleracao * segundos
        if self.velocidade < 0:
            self.velocidade = 0
        print(f"O carro freou e agora está a uma velocidade de {self.velocidade} m/s.")
carro = Carro()
carro.acelerar(5)  
carro.frear(2)     
