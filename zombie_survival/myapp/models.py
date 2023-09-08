from django.db import models

class Item(models.Model):
    nome = models.CharField(max_length=100)
    pontos = models.PositiveIntegerField()

    def __str__(self):
        return self.nome

class Survivor(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1)
    latitude = models.FloatField()
    longitude = models.FloatField()
    infectado = models.BooleanField(default=False)
    itens = models.ManyToManyField(Item)

    def __str__(self):
        return self.nome
