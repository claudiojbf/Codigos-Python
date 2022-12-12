import random

def jogar():
    print("***********************************")
    print("*******Jogo de Adivinhacao!!!******")
    print("***********************************")

    #Variaveis referente ao jogo
    numero_secreto = random.randrange(1, 101)
    total_de_tentativas = 0
    pontos = 1000
    #condicao do while
    condicao = 0
    while (condicao != 1):
        print("Escolha sua dificuldade:")
        print("(1) Facil (2) Medio (3)Dificil")

        dificuldade = int(input("Digite a dificuldade:"))

        if dificuldade == 1:
            total_de_tentativas = 20
            condicao = 1
        elif dificuldade == 2:
            total_de_tentativas = 10
            condicao = 1
        elif dificuldade == 3: 
            total_de_tentativas = 5
            condicao = 1
        else:
            print("Voce digitou uma dificuldade invalida")
            continue

    for rodadas in range(1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodadas, total_de_tentativas))

        chute          = int(input("Digite o seu numero entre 1 e 100: "))
        print("Você digitou: ", chute)

        if(chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 e 100!!")
            continue        

        acertou        = numero_secreto == chute
        chute_maior    = chute > numero_secreto
        chute_menor    = chute < numero_secreto

        
        if acertou:
                print("Voce fez {} pontos".format(pontos))
                break
        else:
                if(chute_maior):
                    print("Voce errou! Você digitou um numero maior")
                elif(chute_menor):
                    print("Voce errou! Você digitou um numero menor")
                    pontos_perdidos = abs(numero_secreto - chute)
                    pontos = pontos - pontos_perdidos
    print("Fim do Jogo")

if (__name__ == "__main__"):
    jogar()