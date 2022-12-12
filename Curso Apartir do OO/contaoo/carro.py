class Carro():
    def __init__(self, cor, modelo, consumo_de_combustivel, capacidade_de_combustivel):
        self.__cor = cor
        self.__modelo = modelo
        self.__consumo_de_combustivel = consumo_de_combustivel
        self.__capacidade_de_combustivel = capacidade_de_combustivel

    def get_cor(self):
        return self.__cor

    def pintar_cor(self, cor):
        if self.__cor == None:
            self.__cor = cor
        else:
            self.remover_cor()
            print("A cor foi removida")
            self.__cor = cor

    def remover_cor(self):
        self.__cor = None

    def get_gasolina(self):
        return self.__capacidade_de_combustivel

    def adquirir_gasolina(self, quantidade):
        trasborda = (self.__capacidade_de_combustivel + quantidade) > 100
        
        if(trasborda):
            print("Quantidade maior que o nescessario")
        else:
            self.__capacidade_de_combustivel += quantidade
    
    def andar(self, distancia):
        consumido = distancia * self.__consumo_de_combustivel
        percorer = consumido <= self.__capacidade_de_combustivel

        if(percorer):
            self.__capacidade_de_combustivel -= consumido
            print("Seu carro percoreu {} km e consumiu {} L de gasolina".format(distancia, consumido))
        else:
            print("Que pena voce ficou sem gasolina não foi possivel terminar o trajeto.")

if __name__ == "__main__":
    carro = Carro("preto", "fiat", 1.5, 30)
    carro.pintar_cor("vermelho")
    print(carro.get_cor())
    carro.adquirir_gasolina(50)
    print(carro.get_gasolina())
    carro.andar(10)

