import math #importar função de cálculo

class Circulo:
    def __init__(self, raio):
        self.raio = raio

    def calcular_area(self):
            return math.pi * (self.raio ** 2)
    
    def calcular_perimetro(self):
         return 2 * math.pi * self.raio