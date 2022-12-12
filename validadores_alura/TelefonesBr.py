import re

class TelefonesBr:
    def __init__(self, telefone):
        if self.valida_telefone(telefone):
            self.numero = telefone
        else:
            raise ValueError("Numero Invalido")

    def __str__(self):
        return self.format_numero()
    
    def valida_telefone(self,telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        respota = re.findall(padrao, telefone)
        if respota:
            return True
        else:
            return False

    def format_numero(self):
        padrao = "([0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        respota = re.search(padrao, self.numero)
        nuemro_formatado = "+{}({}){}-{}".format(
            respota.group(1), 
            respota.group(2), 
            respota.group(3), 
            respota.group(4)
        )

        return nuemro_formatado