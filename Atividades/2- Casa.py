class Imovel:
    def __init__(self,proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel):
        self.proprietrio = proprietario
        self.localizacao = localizacao
        self.quartos = quartos
        self.tamanho = tamanho
        self.banheiros = banheiros
        self.valor_aluguel = valor_aluguel
        self.morador = None
        self.disponibilidade = True

    def imovel_disponivel(self):
        return self.disponibilidade == True

    def alugar(self, novo_morador):
        if self.imovel_disponivel():
            self.morador = novo_morador
            self.disponibilidade = False
        else:
            print("Indisponivel")
    

class Casa(Imovel):
    def __init__(self, proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andares):
        super().__init__(proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel)
        self.andares = andares
        
    def mensagem(self):
        return f"{self.proprietrio}\nAluga-se Casa\nLocalizacao: {self.localizacao}\nQuartos: {self.quartos}\nBanheiros: {self.banheiros}\nAndares: {self.andares}\nAluguel: {self.valor_aluguel}"

class Apartamento(Imovel):
    def __init__(self, proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andar_atual):
        super().__init__(proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel)
        self.andar_atual = andar_atual

    def mensagem(self): 
        return f"{self.proprietrio}\nAluga-se Apartamento\nLocalizacao: {self.localizacao}\nQuartos: {self.quartos}\nBanheiros: {self.banheiros}\nAndar: {self.andar_atual}\nAluguel: {self.valor_aluguel}"

class CasaNova(Casa):
    def __init__(self, proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andares):
        super().__init__(proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andares)
    
    def __str__(self):
        if self.imovel_disponivel():
            return f"Estado: Novo\n{self.mensagem()}" 
        else:
            return "" 

class CasaUsada(Casa):
    def __init__(self, proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andares):
        super().__init__(proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andares)
        self.desconto_aluguel()

    def desconto_aluguel(self):
        desconto = self.valor_aluguel * 0.1
        self.valor_aluguel -= desconto

    def __str__(self):
        if self.imovel_disponivel():
            return f"Estado: Usada\n{self.mensagem()}" 
        else:
            return ""

class ApartamentoNova(Apartamento):
    def __init__(self, proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andar_atual):
        super().__init__(proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andar_atual)
    
    def __str__(self):
        if self.imovel_disponivel():
            return f"Estado: Novo\n{self.mensagem()}" 
        else:
            return ""

class ApartamentoUsada(Apartamento):
    def __init__(self, proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andar_atual):
        super().__init__(proprietario, localizacao, quartos, tamanho, banheiros, valor_aluguel, andar_atual)
        self.desconto_aluguel()

    def desconto_aluguel(self):
        desconto = self.valor_aluguel * 0.1
        self.valor_aluguel -= desconto

    def __str__(self):
        if self.imovel_disponivel():
            return f"Estado: Usada\n{self.mensagem()}" 
        else:
            return ""

casa_centro = CasaNova("AmontadaValley", "Av Jaime", 3, 100, 2, 120, 1)
casa_rua = CasaUsada("AmontadaValley", "Av padre", 3, 100, 2, 120, 1)
apartamento_centro = ApartamentoNova("AmontadaValley", "Av chaves", 3, 100, 2, 120, 1)
apartamento_rua = ApartamentoNova("AmontadaValley", "Av jaime", 3, 100, 2, 120, 1)

casas = [casa_centro, casa_rua, apartamento_centro, apartamento_rua]
apartamento_rua.alugar("Leo")
for a in casas:
    print(a)
apartamento_rua.alugar("Leo")