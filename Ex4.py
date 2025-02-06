class Aluno:
    def __init__(self, nome, matricula, notas):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_situacao(self):
        media = self.calcular_media()
        if media >= 6.0:
            return "Aprovado"
        else:
            return "Reprovado"

aluno = Aluno("Geovanna", "2022001", [7.0, 8.5, 6.0, 5.5])
print(f"Nome: {aluno.nome}")
print(f"Matrícula: {aluno.matricula}")
print(f"Média: {aluno.calcular_media():.2f}")
print(f"Situação: {aluno.verificar_situacao()}")


                 