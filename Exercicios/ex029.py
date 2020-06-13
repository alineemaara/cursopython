velocidade = float(input('Qual velocidade atual do carro? '))
multa = (velocidade -80) * 7
if velocidade >80:
    print('MULTADO! Você execeu o limite permitido de 80Km/h')
    print('Você deve pagar uma multa de R${:.2f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')