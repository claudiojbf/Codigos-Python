class Animais:
    def __init__(self,identificacao, especie, idade, preco, alimentacao, som):
        self.identificacao = identificacao
        self.especie = especie
        self.idade = idade
        self.preco = preco
        self.alimentacao = alimentacao
        self.fome = 0
        self.som = som

    def alimentar(self, alimento):
        if alimento == self.alimentacao:
            self.fome -= 20
            if self.fome <= 0:
                self.fome = 0
                print("O animal saiu de perto")
            else:
                print("Comendo")
        else:
            print("O animal saiu de perto")
    
    def emitir_som(self):
        print(self.som)

class Aereo(Animais):
    def __init__(self, id, especie, alimentacao, idade, preco, som):
        super().__init__(id, especie, idade, preco, alimentacao, som)
        self.vondo = 0

    def voar(self):
        if self.voando == 0:
            print("O passaro esta Voando")
        else:
            print("O passaro ja esta voando")

    def pousar(self):
        if self.voando == 1:
            print("O passaro pousou")
        else:
            print("O passaro ja esta no chao") 

class Terrestre(Animais):
    def __init__(self, id, especie, alimentacao, idade, preco, som):
        super().__init__(id, especie, idade, preco, alimentacao, som)
        self.correndo = 0

    def correr(self):
        if self.correndo == 0:
            print("O animal esta correndo")
            self.correndo = 1
        else:
            print("O animal ja esta correndo")

    def parar(self):
        if self.correndo == 1:
            print("O animal Parou")
            self.correndo = 0
        else:
            print("O animal ja esta parado") 
