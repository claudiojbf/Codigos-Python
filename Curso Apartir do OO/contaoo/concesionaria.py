from time import sleep
class Carro:
    def __init__(self, modelo, ano, preco, chassi, portas, ):
        self._modelo = modelo
        self._ano = ano
        self._preco = preco
        self._chassi = chassi
        self.portas = portas
        self.pneus = 4
        self.numero_de_manutencao = 0
        self.na_concencionaria = True
        self.test_drive = False
        self.quilometros_no_teste = 0.0
        self.placa = None
        self.ipva = None
        self.vendido = False
        self.quilometros_rodados = 0.0

    @property
    def modelo(self):
        return self._modelo
    @property
    def ano(self):
        return self._ano
    @property
    def chassi(self):
        return self._chassi

    @property
    def preco(self):
        return self._preco
    
    @preco.setter
    def preco(self, novo_preco):
        self._preco = novo_preco
    
    def ir_para_concerto(self):
        if self.quilometros_no_teste >= 10.0:
            if self.test_drive == False and self.vendido == False and self.na_concencionaria == True:
                print("O carro saiu para manutencao")
                self.na_concencionaria = False
                self.quilometros_no_teste = 0.0
                self.quilometros_rodados += 0.3
            else:
                print("O carro nao esta disponivel")
        else:
            print("A manutencao ainda nao e nescessaria")

    def voltar_concerto(self):
        if self.test_drive == False and self.vendido == False and self.na_concencionaria == False:
            print("O carro voltou do concerto")
            self.na_concencionaria = True
            self.quilometros_no_teste += 0.3
            self.quilometros_rodados += 0.3
        else:
            print("O carro ainda não foi para o concerto")

    def ir_para_teste(self):
        if self.test_drive == False and self.vendido == False and self.na_concencionaria == True:
            print("O carro saiu para teste")
            self.test_drive == True
            self.quilometros_rodados += 2.0
            self.quilometros_no_teste += 2.0     
        else:
            print("O carro esta indisponivel")
    
    def voltar_teste(self):
        if self.test_drive == True and self.vendido == False and self.na_concencionaria == False:
            print("O carro voltou do teste")
            self.test_drive = False
            self.quilometros_rodados += 2.0
            self.quilometros_no_teste += 2.0
        else:
            print("O carro ainda esta na concesionaria")

    def vender(self):
        if self.test_drive == False and self.vendido == False and self.na_concencionaria == True:
            escolha = input("Voce gostaria de comprar esse carro? (S/N)").upper().strip()
            if escolha == "S":
                print("Parabens voce comprou o carro!!!")
                self.vendido == True
            elif escolha == "":
                print("Que pena, veja mais dos nossos carros!!!")

class Carro_Passeio(Carro):
    def __init__(self, modelo, ano, preco, chassi, portas):
        super().__init__(modelo, ano, preco, chassi, portas)