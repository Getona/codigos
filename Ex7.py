import math

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def se_valido(self):
        if (self.lado1 + self.lado2 > self.lado3 and
            self.lado1 + self.lado3 > self.lado2 and
            self.lado2 + self.lado2 > self.lado1)
        print("É válido")

    def area(self):
            