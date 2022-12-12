from pickle import FALSE
from statistics import quantiles
from tkinter import TRUE


def iniciar():
    cond = False
    while not cond:
        item = input("Qual o Item:\n").upper()
        quantidade = input("Qual a quantidade do {}?\n".format(item))
        registrar(item)
        registrar2(quantidade)        
        sair = input("Gostaria de sair?(S/N)\n").upper().strip()
        if sair == "S":
            cond == True
        else:
            print("Continue Digitando\n")

    inventario = [passar_dados_itens()][passar_dados_quantidade()]

    print(inventario)

def passar_dados_quantidade():
    arquivo2 = open("quantidade.txt", "r")

    quantidade = []

    for linha in arquivo2:
        linha = linha.strip()
        quantidade.append(linha)
   
    arquivo2.close()

    return arquivo2

def passar_dados_itens():
    arquivo1 = open("item.txt","r")
    
    item = []

    for linha in arquivo1:
        linha = linha.strip()
        item.append(linha)

    arquivo1.close()

    return arquivo1

def registrar(item):
    arquivo1 = open("item.txt","w")
    
    arquivo1.write("{}\n".format(item))
    

    arquivo1.close()
    
    
def registrar2(quantidade):
    arquivo2 = open("quantidade.txt", "w")

    arquivo2.write("{}\n".format(quantidade))
    
    arquivo2.close()

if __name__ == "__main__":
    iniciar()