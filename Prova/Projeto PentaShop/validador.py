import re
modelo_email = '[\w]{3,50}(@)(globo|gmail|hotmail|yahoo)(.com)(.br)?'
modelo_nome = '[a-z]{3,}'
nome_email = {}

documento = open("dados.txt", "r")

for linha in documento:
    index = 0
    for texto in linha:
        if texto == ",":
            break
        else:
            index += 1
    new_key = linha[:index]
    new_value = linha[index+1:]
    
    if new_value in nome_email:
        new_documento = open("dados_invalidos.txt", "a")
        new_documento.write(f"{new_key},{new_value}\n")
    else:
        nome_email.update({f"{new_key}":f"{new_value}".replace("\n","")})

for key in nome_email:
    valida_nome = re.search(modelo_nome, key)
    valida_email = re.search(modelo_email, nome_email[key])
    if valida_nome and valida_email: 
        new_documento = open("dados_validos.txt", "a")
        new_documento.write(f"{key},{nome_email[key]}\n")
    else:
        new_documento = open("dados_invalidos.txt", "a")
        new_documento.write(f"{key},{nome_email[key]}\n")
new_documento.close()
documento.close()