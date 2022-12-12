from acesso_cep import BuscaEndereco

from datas_br import DatasBr


"""cadastro = DatasBr()
print(cadastro.mes_cadastro())
print(cadastro.dia_semana())
print(cadastro)
print(cadastro.tempo_cadastro())"""

cep = BuscaEndereco("62540000")

bairro, cidade, uf = cep.acessa_via_cep()

print(bairro, cidade, uf)
