casa = float(input('Valor da Casa: '))
salario = float(input('Salario do Comprador: '))
ano = float(input('Quantos anos de financiamento? '))
prestacao = casa / (ano*12)
minimo = salario*30/100
print('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.' .format(casa,ano,prestacao))
if prestacao > minimo:
    print('Emprestimo NEGADO!!')
else:
    prestacao <= minimo
    print('Emprestimo APROVADO!!')
