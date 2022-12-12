#Crie duas variaveis com valores setados
"""
a = [2,4,6,8,10,12,14,16,18,20]
b = [1,4,8,12,16,18,20]

for x in a:
    if x in b:
        print(f"Valor igual {x}")
"""

class Mulher:
    def __init__(self,idade, estado_civil, cidade, pais):
        self.idade = idade
        self.estado_civil = estado_civil.upper().strip()
        self.cidade = cidade.upper().strip()
        self.pais = pais.upper().strip()
    
    def e_casado(self):
        if self.estado_civil == "CASADA":
            print("Ela e Casada")
        elif self.estado_civil == "SOLTEIRA":
            print("Ela e Solteira")
        else:
            print("Indefinido")
            

    def mora_no_brasil(self):
        if self.pais == "BRASIL":
            print("Mora no Brasil")
        else:
            print(f"Mora no(a) {self.pais}")

def mais_velha(idade1, idade2):
    if idade1 > idade2:
        print(f"A maior idade é {idade1}")
    elif idade1 == idade2:
        print("Tem a mesma idade")
    else:
        print(f"A maior idade é {idade2}")

mulher01 = Mulher(20, "solteira", "amontada", "brasil")
mulher02 = Mulher(30, "casada", "oclaroma", "estados unidos")

mulher01.e_casado()
mulher02.e_casado()

mulher01.mora_no_brasil()
mulher02.mora_no_brasil()

mais_velha(mulher01.idade, mulher02.idade)

