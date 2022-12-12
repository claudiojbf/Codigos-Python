import re

padra_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padra_url.match(self.url)

if not match:
    raise ValueError("A Url nao e valida")

    