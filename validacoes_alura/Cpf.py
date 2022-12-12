from validate_docbr import CPF

class Cpf():
    def __init__(self, documento):
        documento = str(documento)
        self.valida = CPF()
        if self.cpf_e_valido(documento):
            self.cpf = documento
        else:
            raise ValueError("O CPF nao e valido")

    def __str__(self):
        return self.valida.mask(self.cpf)


    def cpf_e_valido(self, documento):
        if len(documento) == 11:
            documento = self.valida.mask(documento)
            return self.valida.validate(documento)
        else:
            return False


    def formata_cpf(self):
        parte_um = self.cpf[0:3]
        parte_dois = self.cpf[3:6]
        parte_tres = self.cpf[6:9]
        parte_quatro = self.cpf[9:]
        return "{}.{}.{}-{}".format(
            parte_um,
            parte_dois,
            parte_tres,
            parte_quatro
        )