class TrianguloInvalidoException(Exception):
    pass

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def tipo_triangulo(self):
        try:
            if self.lado1 <= 0 or self.lado2 <= 0 or self.lado3 <= 0:
                raise TrianguloInvalidoException("Os lados do triângulo devem ser maiores que zero.")
            if self.lado1 + self.lado2 <= self.lado3 or self.lado1 + self.lado3 <= self.lado2 or self.lado2 + self.lado3 <= self.lado1:
                raise TrianguloInvalidoException("Os lados fornecidos não formam um triângulo.")
            
            if self.lado1 == self.lado2 == self.lado3:
                return "Equilátero"
            elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
                return "Isósceles"
            else:
                return "Escaleno"
        except TrianguloInvalidoException as e:
            return str(e)


try:
    tri = Triangulo(3, 4, 5)
    print("Tipo do triângulo:", tri.tipo_triangulo())  
    tri_invalido = Triangulo(1, 2, 3)
    print("Tipo do triângulo:", tri_invalido.tipo_triangulo()) 

except TrianguloInvalidoException as e:
    print("Erro:", e)
