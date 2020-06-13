preco = float(input('Qual valor do produto a prazo?'))
avista = preco - (preco *10/100)
aprazo = preco + (preco *15/100)
print('O valor do produto á vista com 10% de desconto é {:.2f}' .format(avista))
print('O valor do produto a prazo com 15% de acrescimo em 10x é {:.2f}' .format(aprazo))

