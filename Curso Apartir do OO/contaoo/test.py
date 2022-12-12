def criar_conta(numero, titular, saldo, limite):
    conta = {"numero" : numero, "titular" : titular, "saldo" : saldo, "limite" : limite}
    return conta

def depositar(conta, valor):
    conta["saldo"] += valor
    
def sacar(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Seu saldo é R$ {}".format(conta["saldo"]))

conta = criar_conta(321, "Claudio", 100.0, 1000.0)

depositar(conta, 30.0)
extrato(conta)
sacar(conta, 50.0)
extrato(conta)

