from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    biografia = models.TextField(blank=True, null=True)
    idade = models.IntegerField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    escolaridade = models.CharField(max_length=100)
    animais = models.IntegerField(default=0)  # Número de animais

    def __str__(self):
        return self.nome
