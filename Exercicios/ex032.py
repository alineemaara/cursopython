from datetime import date
ano = int(input('Qua ano quer analisar? Coloque 0 para analisar ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100!= 0 or ano % 400== 0:
     print('O ano de {:.0f} é bissexto' .format(ano))
else:
    print('O ano de {:.0f} Não é bissexto' .format(ano))
