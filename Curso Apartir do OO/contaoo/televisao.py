class Televisao:
    def __init__(self, marca, polegadas, cor):
        self.__marca = marca
        self.__polegadas = polegadas
        self.__cor = cor
        self.__canais = {0 : "Pricipal", 1 : "Sbt", 2 : "Record", 3 : "Cultura", 4 : "Globo"}
        self.__canal_atual = 0
        self.__entradas = {0 : "HDMI1", 1 : "HDMI2", 2 : "HDMI3"}
        self.__stado = "off"
        self.__volume = 30

    def ligar(self):
        if self.__stado == "off":
            self.__stado = "on"
            self.__canal_atual = 0
        else:
            self.__stado = "off"

    def trocar_entrada(self):
        if self.__stado == "off":
            print("Por favor ligue a televisao")
        else:
            entradas = [self.__entradas]
            print(entradas)
            print(entradas[0][0])
            print("Selecione qual entrada voce quer:")
            for opcao in entradas[0]:
                print("Entrada {} tipo {}".format(opcao, entradas[0][opcao]))
            escolha = int(input("Qual entrada voce quer?\n"))
            if escolha not in entradas[0]:
                print("Essa Entrada nao existe")
            else:
                print("Voce esta na entrada {}".format(entradas[0][escolha]))
    
    def mutar(self):
        if self.__stado == "off":
            print("Por favor ligue a televisao")
        else:    
            self.__volume = 0

    def aumentar_volume(self):
        if self.__stado == "off":
            print("Por favor ligue a televisao")
        else:
            if self.__volume < 100:
                self.__volume += 1
    
    def diminuir_volume(self):
        if self.__stado == "off":
            print("Por favor ligue a televisao")
        else: 
            if self.__volume == 0:
                self.__volume -= 1

    def mudar_canal(self):
        if self.__stado == "off":
            print("Por favor ligue a televisao")
        else:
            canal = [self.__canais]
            print("Voce esta no canal {}".format(canal[0][self.__canal_atual]))
            print("1. Acima\n2. Abaixo")
            escolha = int(input("Para onde voce gostaria de ir?\n"))
            if escolha == 1:
                self.__canal_atual += 1
                if self.__canal_atual not in canal[0]:
                    print("Assine os nossos pacotes de aumento de canal para liberar mais canais")
                    self.__canal_atual -= 1
                else:
                    print("Voce esta no canal {}".format(canal[0][self.__canal_atual]))
            elif escolha == 2:
                self.__canal_atual -= 1
                if self.__canal_atual not in canal[0]:
                        print("Assine os nossos pacotes de aumento de canal para liberar mais canais")
                        self.__canal_atual += 1
                else:
                        print("Voce esta no canal {}".format(canal[0][self.__canal_atual]))
            else:
                print("Essa opcao não existe")

    

if __name__ == "__main__":
    tv = Televisao("Sansung", 50, "preta")
    tv.ligar()
    tv.trocar_entrada()
    tv.mutar()
    tv.aumentar_volume()
    tv.diminuir_volume()
    tv.mudar_canal()


