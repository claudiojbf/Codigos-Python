url = 'https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100'
print(url)

indice_interogacao = url.find('?')
final_url = len(url)

url_base  = url[0:indice_interogacao]
print(url_base)

url_final = url[indice_interogacao+1:final_url]
print(url_final)