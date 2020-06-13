distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.' .format(distancia))
preco1 = distancia*0.45
preco2 = distancia*0.50
if distancia > 200 :
    print('E o preço da sua passagem será de R${:.2f}' .format(preco1))
else:
    print('E o preço da sua passagem será de R${:.2f}' .format(preco2))
print('Boa Viagem')

#preco = distancia * 0.50 if distancia < 200 else distancia * 0.45

