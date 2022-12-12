from ast import Return
import re
class ExtratorURL:
    def __init__(self,url):
        self.url = url
        self.validar_url()

    def sanitizar_url(self):
        if type(self.url) == str:
            return self.url.strip()
        else:
            return ""
    
    def validar_url(self):
        padra_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padra_url.match(self.url)
        if not match:
            raise ValueError("A Url nao e valida")


    def get_url_base(self):
        indice_interogacao = self.url.find('?')
        url_base = self.url[:indice_interogacao]
        return url_base

    def get_url_parametro(self):
        indice_interogacao = self.url.find('?')
        url_parametro = self.url[indice_interogacao+1:]
        return url_parametro

    def get_valor_parametro(self, nome_parametro):
        indice_parametro = self.get_url_parametro().find(nome_parametro)
        indice_valor = indice_parametro + len(nome_parametro)+1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]

        return valor
    
    def converter_dolar(self,origem, destino, quantidade):
        VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
        if origem == "dolar" and destino == "real":
            valor_convertido = float(quantidade) * VALOR_DOLAR
            return valor_convertido
        elif origem == "real" and destino =="dolar":
            valor_convertido = float(quantidade)/VALOR_DOLAR
            return valor_convertido

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)

VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")

print(extrator_url.converter_dolar(moeda_destino, moeda_origem, quantidade))
