from sqlite3 import DatabaseError


def inicio():
    database = [[], [], []]
    cond = False
    while not cond:
        nome = input("Digite seu nome\n").upper()
        endereco = input("Digite seu Endereco\n").upper()
        cadastro(nome, endereco, database)
        sair = input("Voce Gostaria de Sair?(S/N)\n").upper()
        if sair == "S":
            cond = True
        else:
            print("Continue Digitando")
    print(database)

def cadastro(nome, endereco, database):
    ident = 0
    database[0] = ident    
    for posicao in range(0, len(database[0])):
        database[0].append(database[0][posicao] + 1)
    database[1].append(nome)
    database[2].append(endereco)
    return database

if __name__ == "__main__":
    inicio()