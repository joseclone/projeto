from django.db import models
from django.utils.timezone import datetime
# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=20)
    descricao = models.TextField(default='Descreva sobre seu produto')
    quantidade = models.IntegerField(default=0)
    data = models.DateField(default=datetime.now)
    # texto = models.TextField()

    def __str__(self):
        return self.nome