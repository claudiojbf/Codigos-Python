

class Conta():
    def __init__(self, numero, titular, saldo, limite):
        print("Conta acessada ...")
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
    
    def extrato(self):
        print("O extrato do cliente {} e R$ {} reais". format(self.__titular, self.__saldo))
    
    def deposito(self, valor):
        self.__saldo += valor
    
    def __pode_sacar(self, valor):
        valor_disponivel = self.__saldo + self.__limite
        return valor <= valor_disponivel

    def saque(self, valor):
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou do limite.".format(valor))
    
    def trasfere(self, valor, destino):
        self.saque(valor)
        destino.deposito(valor)

    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @staticmethod
    def codigo_banco():
        return "001"
    
    @staticmethod
    def codigos_bancos():
        return {"BB" : "001", "Bradesco" : "237", "Caixa" : "103"}
    


if __name__ == "__main__":
    from conta import Conta
    conta = Conta(123, "Claudio", 60.0, 1000.0)
    conta2 = Conta(321, "Leo", 100.0, 1000.0)

    print(conta.titular)
    print(conta.saldo)
    print(conta.limite)
    conta.limite = 10000.0
    print(conta.limite)