class Retângulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura #Conta para calcular área

    def calcular_perimetro(self):
        return 2 * (self.largura + self.altura) #Conta para calcular perímetro

retangulo = Retângulo(5, 10)
print(f'Área do retângulo: {retangulo.calcular_area()}')  
print(f'Perímetro do retângulo: {retangulo.calcular_perimetro()}')  
