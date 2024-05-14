class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return 3.14 * (self.raio ** 2)
circulo = Circulo(5)
area_circulo = circulo.area()
print(f"A área do círculo com raio {circulo.raio} é {area_circulo:.2f}.")
