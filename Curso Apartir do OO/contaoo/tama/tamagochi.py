from time import sleep

class Tama():
    def __init__(self, nome):
        self.__nome = nome
        self.__xp = 0
        self.__fome = 0
        self.__energia = 100
        self.__sede = 0
        self.__saude = 100
        self.__humor = 100
        self.__idade = 0

    def __ganha_xp(self, valor):
        self.__xp += valor

        if self.__xp >= 100:
            self.__idade +=1
            self.__xp = 0

    def __alterar_fome(self, valor):
        if valor == 1:
            self.__fome += 10
        elif valor == 2:
            self.__fome -= 5

        if self.__fome < 0:
            self.__fome = 0
            print("Estou cheio!")
            sleep(0.8)
            self.__alterar_saude(2, 2)    
        elif self.__fome > 100:
            self.__fome = 100
            print("Estou com muita fome")
            sleep(0.8)
            self.__alterar_saude(2, 2)           
    
    def __alterar_energia(self, valor):
        if valor == 1:
            self.__energia += 5
        elif valor == 2:
            self.__energia -= 10
        elif valor == 3:
            self.__energia += 20

        if self.__energia > 100:
            self.__energia = 100
            print("Estou eletrico de mais!!!!")
            sleep(0.8)
            self.__alterar_saude(2, 2) 
        elif self.__energia < 0:
            self.__energia = 0
            print("Estou muito cansado")
            sleep(0.8)
            self.__alterar_saude(2, 2)

        if self.__energia < 30:
            self.__alterar_humor(2)

    def __alterar_sede(self, valor):
        if valor == 1:
            self.__sede += 10
        else:
            self.__sede -= 5

        if self.__sede > 100:
            self.__sede = 100
            self.__alterar_saude(2, 2) 
        elif self.__sede < 0:
            self.__sede = 0
            self.__alterar_saude(2, 2)

    def __alterar_saude(self, valor, valor2):
        if valor == 1:
            self.__saude += 5
        elif valor == 2:
            self.__saude -= 10
        
        if valor2 == 1: 
            if self.__saude > 100:
                self.__saude -= 45
        else:
            self.__saude = 100
   
    def __alterar_humor(self, valor):
        if valor == 1:
            self.__humor += 5
        else:
            self.__humor -= 5
        
        if self.__humor > 100:
            self.__humor = 100
        if self.__humor < 0:
            self.__humor = 0
            self.__alterar_saude(2, 2)

    def fase(self):
        if self.__idade < 5:
            print("Bebe")
        elif self.__idade < 10:
            print("Crianca")
        elif self.__idade < 15:
            print("Adolecente")
        elif self.__idade < 20:
            print("Adulto")
        elif self.__idade < 25:
            print("Idoso")

    def morto(self):
        return self.__saude <= 0 or self.__idade == 25

    def dormir(self):
        if self.__energia > 50:
            self.__alterar_humor(2)
            print("Eu não quero dormir :(")
            sleep(0.8)
        else:
            print("ZzZz")
            sleep(1)
            print("ZzZZ")
            sleep(1)
            print("ZZZz")
            sleep(1)

            self.__alterar_energia(3)
            self.__alterar_fome(1)
            self.__alterar_sede(1)
    
    def se_alimenta(self):
        print("Comendo...")
        sleep(2)
        self.__alterar_energia(1)
        self.__alterar_fome(2)
        self.__ganha_xp(2)

    def beber_agua(self):
        print("Tomando Agua...")
        sleep(0.5)
        self.__alterar_sede(2)
        self.__ganha_xp(1)

    def tomar_remedio(self):
        print("Tomando remedio")
        sleep(0.2)
        self.__alterar_saude(1, 1)
    
    def bricar(self):
        print("Esta Brincando...")
        sleep(0.5)
        self.__alterar_energia(2)
        self.__alterar_fome(1)
        self.__alterar_sede(1)
        self.__ganha_xp(3)

    def jogar(self):
        ativo = 1
        while ativo == 1:
            print("               {}               ".format(self.__nome))
            if self.morto():
                print("Aqui jaz...\n  {self.__nome}")
                break
            else:
                print("Saude: {}  Energia: {} Fome: {}  Sede: {}  Humor: {} Idade: {}".format(self.__saude, self.__energia, self.__fome, self.__sede, self.__humor, self.__idade))
                print("")
                print("")
                print("")
                self.fase()
                print("")
                print("")
                print("")

                print("Atividades:")
                print("0. Dormir  1. Brincar  2. Alimentar-se  3. Beber Agua 4. Tomar Remedio")
                escolha = int(input(""))
                if escolha < 0 or escolha > 4:
                    print("Opcão Invalida")
                else:
                    if escolha == 0:
                        self.dormir()
                    elif escolha == 1:
                        self.bricar() 
                    elif escolha == 2:
                        self.se_alimenta() 
                    elif escolha == 3:
                        self.beber_agua() 
                    elif escolha == 4:
                        self.tomar_remedio() 

if __name__ == "__main__":
    tama =  Tama("Luke")
    tama.jogar()