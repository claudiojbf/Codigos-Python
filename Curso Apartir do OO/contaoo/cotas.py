
class Participantes:
    def __init__(self,nome, dinheiro):
        self.nome = nome
        self.dinheiro = dinheiro
        self.pagou = [0, 0, 0, 0]
        self.pontos_turisticos = 0

    def pagar_cota(self, valor):
        if self.dinheiro >= valor:
            self.dinheiro -= valor
            self.pagou[self.pontos_turisticos] = 1
            self.pontos_turisticos += 1 
        else:
            print("Dinheiro insuficiente")

    def escolher_passeio(self):
        pontos = ["Maracana", "Pao de Acucar", "Cristo Redentor", "Rosinha"]
        print(self.nome)
        for p in pontos:
            escolha = input(f"Voce Gostaria de ir para {p}? (S/N)").upper().strip()
            if escolha == "S":
                self.pagar_cota(200)
            else:
                self.pontos_turisticos += 1 
            print("proximo...")

class Viagem:
    def __init__(self, lista_de_passageiros):
        self.lista_de_passageiros = lista_de_passageiros
        self.maracana = []
        self.pao_de_acuca = []
        self.cristo_redentor = []
        self.rocinha = []
    

    def conferir_participantes(self):
        for a in self.lista_de_passageiros:
            print(a.pagou)
            if a.pagou[0] == 1:
                self.maracana.append(a.nome)
            if a.pagou[1] == 1:
                self.pao_de_acuca.append(a.nome)
            if a.pagou[2] == 1:
                self.cristo_redentor.append(a.nome)
            if a.pagou[3] == 1:
                self.rocinha.append(a.nome)
    
    def listar_passeios(self):
        print("Maracana: ")
        for a in self.maracana:
            print(a)
        print("pao_de_acucar: ")
        for a in self.pao_de_acuca:
            print(a)
        print("cristo_redentor: ")
        for a in self.cristo_redentor:
            print(a)
        print("rocinha: ")
        for a in self.rocinha:
            print(a)

p1 = Participantes("C1", 1000)
p1.escolher_passeio()

p2 = Participantes("C2", 1000)
p2.escolher_passeio()

'''p3 = Participantes("C3", 3000)
p3.escolher_passeio()

p4 = Participantes("C4", 1000)
p4.escolher_passeio()

p5 = Participantes("C5", 1000)
p5.escolher_passeio()

p6 = Participantes("C6", 1000)
p6.escolher_passeio()

p7 = Participantes("C7", 1000)
p7.escolher_passeio()

p8 = Participantes("C8", 1000)
p8.escolher_passeio()

p9 = Participantes("C9", 1000)
p9.escolher_passeio()

p10 = Participantes("C10", 1000)
p10.escolher_passeio()

p11 = Participantes("C11", 1000)
p11.escolher_passeio()

p12 = Participantes("C12", 1000)
p12.escolher_passeio()

p13 = Participantes("C13", 1000)
p13.escolher_passeio()

p14 = Participantes("C14", 1000)
p14.escolher_passeio()

p15 = Participantes("C15", 1000)
p15.escolher_passeio()

p16 = Participantes("C16", 1000)
p16.escolher_passeio()

p17 = Participantes("C17", 1000)
p17.escolher_passeio()

p18 = Participantes("C18", 1000)
p18.escolher_passeio()

p19 = Participantes("C19", 1000)
p19.escolher_passeio()

p20 = Participantes("C20", 1000)
p20.escolher_passeio()

p21 = Participantes("C21", 1000)
p21.escolher_passeio()

p22 = Participantes("C22", 1000)
p22.escolher_passeio()

p23 = Participantes("C23", 1000)
p23.escolher_passeio()

p24 = Participantes("C24", 1000)
p24.escolher_passeio()

p25 = Participantes("C25", 1000)
p25.escolher_passeio()

p26 = Participantes("C26", 1000)
p26.escolher_passeio()

p27 = Participantes("C27", 1000)
p27.escolher_passeio()

p28 = Participantes("C28", 1000)
p28.escolher_passeio()

p29 = Participantes("C29", 1000)
p29.escolher_passeio()

p30 = Participantes("C30", 1000)
p30.escolher_passeio()
'''

viajantes = [p1, p2]
''', p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16, p17, p18, p19, p20, p21, p22, p23, p24, p25, p26, p27, p28, p29, p30'''
v1 = Viagem(viajantes)

v1.conferir_participantes()
v1.listar_passeios()