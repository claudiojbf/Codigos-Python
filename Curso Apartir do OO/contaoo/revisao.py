class Funcionario:
    def __init__(self, nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo):
        self.nome = nome
        self._cpf = cpf
        self._matricula = matricula
        self._horario_entrada = horario_entrada
        self._horario_saida = horario_saida
        self.contato = contato
        self.data_nascimento = data_nascimento
        self.estado_civil = estado_civil
        self.sexo = sexo
        self._bonus = 0.0

    @property
    def cpf(self):
        return self._cpf

    @property
    def matricula(self):
        return self._matricula

    @matricula.setter
    def matricula(self, matricula):
        self._matricula = matricula

    @property
    def horario_entrada(self):
        return self._horario_entrada
        
    @horario_entrada.setter
    def horario_entrada(self, horario_entrada):
        self._horario_entrada = horario_entrada

    @property
    def horario_saida(self):
        return self._horario_saida
        
    @horario_saida.setter
    def horario_saida(self, horario_saida):
        self._horario_saida = horario_saida

    @property
    def bonus(self):
        return self.bonus
    @bonus.setter
    def bonus(self, vendas):
        self._bonus = self._bonificacao * vendas

class Gerente(Funcionario):
    def __init__(self, nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo):
        super().__init__(nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo)            
        self._salario = 3000.00
        self._bonificacao = 0.2


    @property
    def salario(self):
        return self._salario

    @property
    def bonificacao(self):
        return self._bonificacao    
        


class Atendente(Funcionario):
    def __init__(self, nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo):
        super().__init__(nome, cpf, matricula, horario_entrada, horario_saida, contato, data_nascimento, estado_civil, sexo)
        self._salario = 1200.00
        self._bonificacao = 0.1
        

    @property
    def salario(self):
        return self._salario

    @property
    def bonificacao(self):
        return self._bonificacao
        


atendente = Atendente("Barbie", 12340000165, 101010, "8:00", "18:00", "40028922",
    "01/09/1500", "casada", "F")

atendente2 = Atendente("Roberto", 12340000164, 101510, "14:00", "22:00", "40028923",
    "02/09/1500", "solteiro", "M")

print(atendente.cpf)
print(atendente2.matricula)

atendente2.matricula = "253639"
print(atendente2.matricula)
