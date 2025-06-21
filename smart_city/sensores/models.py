from django.db import models

class Ambiente(models.Model):
    sig = models.IntegerField(primary_key=True)
    descricao = models.CharField(max_length=100)
    ni = models.CharField(max_length=20)
    responsavel = models.CharField(max_length=100)

class Sensor(models.Model):
    sensor = models.CharField(max_length=50, primary_key=True)
    mac_address = models.CharField(max_length=50)
    unidade_med = models.CharField(max_length=20)
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.BooleanField(default=True)

class Historico(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    ambiente = models.ForeignKey(Ambiente, on_delete=models.CASCADE)
    valor = models.FloatField()
    timestamp = models.IntegerField()
