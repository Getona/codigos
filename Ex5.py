class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_salario_liquido(self, imposto, beneficio):
        salario_liquido = self.salario - (self.salario * imposto / 100) + beneficio
        return salario_liquido

funcionario = Funcionario("Ana", 5000.00, "Desenvolvedora")
imposto = 15.0 
beneficio = 300.00  

print(f"Nome: {funcionario.nome}")
print(f"Cargo: {funcionario.cargo}")
print(f"Salário Bruto: R${funcionario.salario:.2f}")
print(f"Salário Líquido: R${funcionario.calcular_salario_liquido(imposto, beneficio):.2f}")
