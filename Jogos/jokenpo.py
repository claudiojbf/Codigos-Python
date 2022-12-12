import random
import time

def inicio():
    mensagem_bem_vindo()
    mensagem_de_apresentacao()
    escolha = int(input("Digite a sua escolha:\n"))
    if escolha < 1 or escolha > 3:
        print("Digite um numero entre 1 e 3!!")
    else:
        oponente = escolha_do_oponente()
        jogar(escolha, oponente)
    

def jogar(escolha, oponente):
    jokenpo = ["PEDRA", "PAPEL", "TESOURA"]
    chamar_jokenpo()
    if escolha == oponente:
        print("Voce escolheu {} e seu oponente escolheu {}.".format(jokenpo[escolha-1],jokenpo[oponente-1]))
        print("Empate!!")
    elif escolha == 1 and oponente == 2:
        print("Voce escolheu {} e seu oponente escolheu {}.".format(jokenpo[escolha-1],jokenpo[oponente-1]))
        print("GAME OVER!")
    elif escolha == 2 and oponente == 3:
         print("Voce escolheu {} e seu oponente escolheu {}.".format(jokenpo[escolha-1],jokenpo[oponente-1]))
         print("GAME OVER!")
    elif escolha == 3 and oponente == 1:
         print("Voce escolheu {} e seu oponente escolheu {}.".format(jokenpo[escolha-1],jokenpo[oponente-1]))
         print("GAME OVER!")
    elif escolha == 2 and oponente == 1:
         print("Voce escolheu {} e seu oponente escolheu {}.".format(jokenpo[escolha-1],jokenpo[oponente-1]))
         print("WIN!!!")
    elif escolha == 3 and oponente == 2:
         print("Voce escolheu {} e seu oponente escolheu {}.".format(jokenpo[escolha-1],jokenpo[oponente-1]))
         print("WIN!!!")
    elif escolha == 1 and oponente == 3:
         print("Voce escolheu {} e seu oponente escolheu {}.".format(jokenpo[escolha-1],jokenpo[oponente-1]))
         print("WIN!!!")
    time.sleep(0.5)

def chamar_jokenpo():
    print("Jo")
    time.sleep(0.5)
    print("Ken")
    time.sleep(0.5)
    print("Po!!!")
    time.sleep(0.5)

def escolha_do_oponente():
    oponente = random.randint(1,4)
    return oponente

def mensagem_de_apresentacao():
    print("Vamos Jogar Jo Ken Po!")
    print("Selecione entre:\n 1.Pedra \n 2.Papel \n 3.Tesoura")

def mensagem_bem_vindo():
    print("***************************************************")
    print("+++++++++++++++Jo Ken Po!!!!!!+++++++++++++++++++++")
    print("***************************************************")

if __name__ == "__main__":
    inicio()