from django.shortcuts import render, get_object_or_404
from .models import Conta
from app_cliente.models import Cliente
from app_deposito.models import Deposito,ContadorDeposito
from app_trasferencia.models import Trasferencia, ContadorTrasferencia

def conta(request, id):
    cliente = get_object_or_404(Cliente, pk=id)
    conta = get_object_or_404(Conta, usuario = cliente)
    depositos = Deposito.objects.all().filter(conta = conta)
    contador_dep = get_object_or_404(ContadorDeposito, conta = conta)
    trasferencias = Trasferencia.objects.all().filter(conta = conta)
    contador_trasf = get_object_or_404(ContadorTrasferencia, conta = conta)
    
    valor_depositos = 0
    valor_gastos = 0
    for deposito in depositos:
        valor_depositos += deposito.valor
    if contador_dep.numero_depositos < depositos.count():
        if contador_dep.valor_ult < valor_depositos:
            valor_dif = valor_depositos - contador_dep.valor_ult
            conta.saldo +=  valor_dif
            conta.save()
            contador_dep.numero_depositos = depositos.count()
            contador_dep.valor_ult = valor_depositos
            contador_dep.save()
    for trasferencia in trasferencias:
        valor_gastos += trasferencia.valor
    if contador_trasf.numero_trasferencias < trasferencias.count():
        if contador_trasf.valor_ultimas < valor_gastos:
            valor_dif = valor_gastos - contador_trasf.valor_ultimas
            conta.saldo -= valor_dif
            conta.save()
            contador_trasf.numero_trasferencias = trasferencias.count()
            contador_trasf.valor_ultimas = valor_gastos
            contador_trasf.save()
    
    dados = {
        'conta' : conta,
        'depositos' : depositos,
        'gastos' : valor_gastos,
    }
    return render(request, 'index.html', dados)
