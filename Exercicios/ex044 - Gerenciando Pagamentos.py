print('================= LOJAS MARA ===================')
compra = float(input('Qual valor da compra: '))
print('''FORMAS DE PAGAMENTO: 
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x cartão
[4] 3x ou mais no cartão''')
opcao = int(input('Qual é opção: '))
if opcao == 1 :
    total = compra - (compra*10 /100)
elif opcao == 2 :
    total = compra - (compra*5 /100)
elif opcao == 3 :
    total = compra
    parcela = total / 2
    print('Sua compra será parcelada em 2x de {:.2f} SEM JUROS.'.format(parcela))
elif opcao == 4 :
    total = compra + (compra * 20/100)
    parcela = int(input('Quantas parcelas? '))
    totparc = total / parcela
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcela,totparc))
else:
    total = compra
    print('Opcão INVALIDA, TENTE NOVAMENTE!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra,total))
