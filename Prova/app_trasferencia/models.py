from django.db import models
from django.forms import FloatField
from app_conta.models import Conta

class Trasferencia(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    descricao = models.CharField(max_length=100)
    valor = models.FloatField()

class ContadorTrasferencia(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    numero_trasferencias = models.IntegerField()
    valor_ultimas = models.FloatField()
