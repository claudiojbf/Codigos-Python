import forca
import adivinhacao

def escolha_jogo():
    print("***********************************")
    print("********Escolha o seu Jogo!********")
    print("***********************************")

    print("(1) Forca (2) Adivinhacao")

    condicao = 0
    while (condicao != 1):
        jogo = int(input("Qual o seu Jogo? "))

        if(jogo == 1):
            forca.jogar()
            condicao = 1
        elif(jogo == 2):
            adivinhacao.jogar()
            condicao = 1
        else:
            print("Opcao indisponivel escolha outra!!!")
            continue

if(__name__ == "__main__"):
    escolha_jogo()