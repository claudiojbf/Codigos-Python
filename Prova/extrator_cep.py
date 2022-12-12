import re
endereco = "Av Jaime Assis Henrique 365, Centro, Amontada, CE, 62540000"

padrao = re.compile('[0-9]{5}[-]?[0-9]{3}')
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)