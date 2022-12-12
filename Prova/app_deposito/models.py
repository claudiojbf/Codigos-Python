from django.db import models
from app_conta.models import Conta

class Deposito(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()

    def __str__(self):
        return self.conta.usuario.nome

class ContadorDeposito(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    numero_depositos = models.IntegerField()
    valor_ult = models.FloatField()