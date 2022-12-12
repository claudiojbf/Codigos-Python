def cadastro_masculino():
    categoria = input("Qual a categoria da roupa?")
    nome = input("Qual o nome da peca?")
    preco = float(input("Qual o preco da peca?".format(".2f")))
    questiona = int(input("Quantos tamanhos tera disponivel?(1 a 3)"))
    if questiona == 1:
        tamanho = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        if tamanho == "P" or "M" or "G":
            print("="*20)
            print("Cadastro Realizado com sucesso")
            print("="*20)
        else:
            raise ValueError("Tamanho Invalido")
    elif questiona == 2:
        tamanho = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        tamanho2 = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        if tamanho == "P" or "M" or "G" and tamanho2 == "P" or "M" or "G":
            print("Peca cadastrada com sucesso")
        else:
            raise ValueError("Tamanho Invalido")
    elif questiona == 3:
        tamanho = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        tamanho2 = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        tamanho3 = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        if tamanho == "P" or "M" or "G" and tamanho2 == "P" or "M" or "G" and tamanho3 == "P" or "M" or "G":
            print("Peca cadastrada com sucesso")
        else:
            raise ValueError("Tamanho Invalido")
    else:
        raise ValueError("Opcao invalida")
    
    cadastro = open("masculino.txt", "a")
    if questiona == 1:
        cadastro.write(f"{categoria}-{nome}-{preco}-{tamanho}\n")
    elif questiona == 2:
        cadastro.write(f"{categoria}-{nome}-{preco}-{tamanho}-{tamanho2}\n")
    elif questiona == 3:
        cadastro.write(f"{categoria}-{nome}-{preco}-{tamanho}-{tamanho2}-{tamanho3}\n")
    cadastro.close()

def cadastro_feminino():
    categoria = input("Qual a categoria da roupa?")
    nome = input("Qual o nome da peca?")
    preco = float(input("Qual o preco da peca?".format(".2f")))
    questiona = int(input("Quantos tamanhos tera disponivel?(1 a 3)"))
    if questiona == 1:
        tamanho = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        if tamanho == "P" or "M" or "G":
            print("="*20)
            print("Cadastro Realizado com sucesso")
            print("="*20)
        else:
            raise ValueError("Tamanho Invalido")
    elif questiona == 2:
        tamanho = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        tamanho2 = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        if tamanho == "P" or "M" or "G" and tamanho2 == "P" or "M" or "G":
            print("Peca cadastrada com sucesso")
        else:
            raise ValueError("Tamanho Invalido")
    elif questiona == 3:
        tamanho = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        tamanho2 = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        tamanho3 = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        if tamanho == "P" or "M" or "G" and tamanho2 == "P" or "M" or "G" and tamanho3 == "P" or "M" or "G":
            print("Peca cadastrada com sucesso")
        else:
            raise ValueError("Tamanho Invalido")
    else:
        raise ValueError("Opcao invalida")
    
    cadastro = open("feminino.txt", "a")
    if questiona == 1:
        cadastro.write(f"{categoria}-{nome}-{preco}-{tamanho}\n")
    elif questiona == 2:
        cadastro.write(f"{categoria}-{nome}-{preco}-{tamanho}-{tamanho2}\n")
    elif questiona == 3:
        cadastro.write(f"{categoria}-{nome}-{preco}-{tamanho}-{tamanho2}-{tamanho3}\n")
    cadastro.close()

def cadastro_infantil():
    categoria = input("Qual a categoria da roupa?")
    nome = input("Qual o nome da peca?")
    preco = float(input("Qual o preco da peca?".format(".2f")))
    questiona = int(input("Quantos tamanhos tera disponivel?(1 a 3)"))
    if questiona == 1:
        tamanho = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        if tamanho == "P" or "M" or "G":
            print("="*20)
            print("Cadastro Realizado com sucesso")
            print("="*20)
        else:
            raise ValueError("Tamanho Invalido")
    elif questiona == 2:
        tamanho = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        tamanho2 = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        if tamanho == "P" or "M" or "G" and tamanho2 == "P" or "M" or "G":
            print("Peca cadastrada com sucesso")
        else:
            raise ValueError("Tamanho Invalido")
    elif questiona == 3:
        tamanho = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        tamanho2 = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        tamanho3 = input("Digite o tamanho disponivel(P, M, G)").upper().strip()
        if tamanho == "P" or "M" or "G" and tamanho2 == "P" or "M" or "G" and tamanho3 == "P" or "M" or "G":
            print("Peca cadastrada com sucesso")
        else:
            raise ValueError("Tamanho Invalido")
    else:
        raise ValueError("Opcao invalida")
    
    cadastro = open("infantil.txt", "a")
    if questiona == 1:
        cadastro.write(f"{categoria}-{nome}-{preco}-{tamanho}\n")
    elif questiona == 2:
        cadastro.write(f"{categoria}-{nome}-{preco}-{tamanho}-{tamanho2}\n")
    elif questiona == 3:
        cadastro.write(f"{categoria}-{nome}-{preco}-{tamanho}-{tamanho2}-{tamanho3}\n")
    cadastro.close()

def cadastro_acessorios():


    categoria = input("Qual a categoria do acessorio?")
    nome = input("Qual o nome da peca?")
    preco = float(input("Qual o preco da peca?".format(".2f")))
    print("="*20)
    print("Cadastro Realizado com sucesso")
    print("="*20)
    
    cadastro = open("acessorios.txt", "a")
    cadastro.write(f"{categoria}-{nome}-{preco}-U\n")
    cadastro.close()
    
def deleta():
    questao = input("De qual arquivo Voce gostaria de deletar?(Masculino(M) Feminino(F) Infantil (F) Acessorio(A))").upper().strip()
    if questao == "M":
        opcao = "masculino"
    elif questao == "F":
        opcao = "feminino"
    elif questao == "I":
        opcao = "infantil"
    elif questao == "A":
        opcao = "acessorios"   
    else:
        raise ValueError("Opcao invalida")
    
    indice = 0
    lista = []
    arquivo = open(f"{opcao}.txt", "r")
    for a in arquivo:
        print(f"{indice} - {a}")
        indice += 1
        lista.append(a)
    arquivo.close()

    item = int(input("Qual item deseja excluir?"))
    del lista[item]
    
    arquivo = open(f"{opcao}.txt", "w")
    for a in lista:
        arquivo.write(f"{a}")
        
    arquivo.close()

#cadastro_masculino()
#cadastro_feminino()
#cadastro_infantil()
cadastro_acessorios()
cadastro_acessorios()
deleta()

