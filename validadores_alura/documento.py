from validate_docbr import CPF,CNPJ

class Documento():
    def __init__(self, documento):
        documento = str(documento)
        self.qual_documento(documento)
        self.documento_final(documento)
    

    def qual_documento(self,documento):
        if len(documento) == 11:
            self.valida = CPF()
        elif len(documento) == 14:
            self.valida = CNPJ()
        else:
            raise ValueError("Documento Invalido")

    def __str__(self):
        return self.formata_cpf()

    def documento_final(self, documento):
        if len(documento) == 11:
            if self.cpf_e_valido(documento):
                self.documento = documento
        elif len(documento) == 14:
            if self.cnpj_e_valido(documento):
                self.documento = documento
        else:
            raise ValueError("Documento invalido!!!")

    def cpf_e_valido(self, documento):
        if len(documento) == 11:
            documento = self.valida.mask(documento)
            return self.valida.validate(documento)
        else:
            raise("Numero de digitos invalido!!!")
    
    def cnpj_e_valido(self, documento):
        if len(documento) == 14:
            documento = self.valida.mask(documento)
            return self.valida.validate(documento)
        else:
            raise ValueError("Numero de digitos invalio!!!")


    def formata(self):
      return self.valida.mask(self.documento)


    def __str__(self):
        return self.formata()