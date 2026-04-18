#url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
url = " "

#sanitização da URL
url = url.strip()


#validação da URL
if url == "":
    raise ValueError("A URL esta vazia")

# Separa base e os parametros
indice_interrogacao = url.find('?')

url_base = (url[:indice_interrogacao])
url_parametros = url[indice_interrogacao+1:]
print(url_parametros)


#busca o valor de um parametro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)

indice_valor = indice_parametro + len(parametro_busca)+ 1
indice_E_comercial = url_parametros.find('&', indice_valor)
if indice_E_comercial == -1:
    valor = url_parametros[indice_valor:indice_E_comercial:]
else:
    valor = url_parametros[indice_valor:indice_E_comercial]

print(valor)


