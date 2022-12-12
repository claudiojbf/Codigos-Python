

class Pessoa:
    def __init__(self, nome, idade, altura, genero):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.genero = genero

    def de_maior(self):
        if self.idade >= 18:
            print("{} tem {} anos então ele e de maior".format(self.nome, self.idade))
        else:
            print("{} tem {} anos então ele e de menor".format(self.nome, self.idade))

    def estatura_media(self):
        if self.altura >= 1.65 and self.altura <= 1.75:
            print("Sua altura e {} entao voce tem um estarua media.".format(self.altura))
        else:
            print("Sua altura e {} entao voce nao tem um estarua media.".format(self.altura))
            

    def fase_da_pessoa(self):
        if self.idade <= 12:
            print("Voce e uma crianca.")
        elif self.idade > 12 and self.idade < 18:
            print("Voce e um adolecente.")
        elif self.idade >=18 and self.idade < 60:
            print("Voce e um adulto.")
        elif self.idade >= 60 and self.idade < 100:
            print("Voce e um idoso")
        else:
            print("Você é um anciao.")