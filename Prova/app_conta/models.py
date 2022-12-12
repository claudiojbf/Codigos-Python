from django.db import models
from app_cliente.models import Cliente

class Conta(models.Model):
    numero_conta = models.IntegerField()
    saldo = models.FloatField()
    usuario = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.usuario.nome