import re
class MinhaAgenda:
    def __init__(self, nome, end, email, numero_de_contato):
        self._nome = nome
        self.end = end
        self.email = email
        self.numero_de_contato = numero_de_contato

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

class PessoaFisica(MinhaAgenda):
    def __init__(self, nome, end, email, numero_de_contato, cpf, data_de_nascimento):
        super().__init__(nome, end, email, numero_de_contato)
        self._cpf = cpf
        self.valida_cpf()
        self.data_de_nascimento = data_de_nascimento    

    def valida_cpf(self):
        padrao = re.compile("[0-9]{3}[.]?[0-9]{3}[.]?[0-9]{3}[-]?[0-9]{2}")
        busca = padrao.match(self._cpf)

        if not busca:
            raise ValueError("O Cpf nao e Valido")
        
        print("Cpf Valido")
    
    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, novo_cpf):
        self._cpf = novo_cpf

class PessoaJuridica(MinhaAgenda):
    def __init__(self, nome, end, email, numero_de_contato, cnpj):
        super().__init__(nome, end, email, numero_de_contato)
        self._cnpj = cnpj
        self.validar_cnpf()
    
    @property
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj

    def validar_cnpf(self):
        padrao = re.compile("[0-9]{2}[.]?[0-9]{3}[.]?[0-9]{3}[/]?[0]{3}[0-9][-]?[0-9]{2}")
        match = padrao.match(self._cnpj)

        if not match:
            raise ValueError("O cnpj nao e valido")
        
        print("Cnpj Valido")

pessoa = PessoaFisica("Claudio","Av Jaime","brosson123", "859999999", "04164892307","11/07/2000",)
juridico = PessoaJuridica("ataca","rua padre","ataca123","85999999999","27.123.321/00011-27")