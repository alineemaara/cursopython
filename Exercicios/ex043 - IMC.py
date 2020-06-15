peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura? '))
imc = peso / (altura*altura)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5 :
    print('Você está ABAIXO DO PESO normal.')
elif imc >= 18.5 and imc < 25:
    print('PARABENS, Você está no PESO IDEAL.')
elif imc >= 25 and imc < 30 :
    print('Você está com SOBREPESO.')
elif imc >= 30 and imc < 40:
    print('Você está com OBESIDADE!')
else:
    print('Você está com OBESIDADE MORBIDA, cuidado!')