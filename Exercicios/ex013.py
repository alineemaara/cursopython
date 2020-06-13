salario = float(input('Qual é salario do funcionario?'))
novo = salario + (salario * 15/100)
print('Salario atual R${:.2f} com aumento de 15% {:.2f}'.format(salario,novo))
