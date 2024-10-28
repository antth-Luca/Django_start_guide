from django.db import models
from Cidade.models import Cidade

# Create your models here.
class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nome}'