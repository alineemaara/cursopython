primeiro = int(input('Primeiro Valor: '))
segundo = int(input('Segundo valor: '))
terceiro = int(input('Terceiro valor: '))
maior = primeiro
if (segundo > maior):
    maior = segundo
if (terceiro > maior):
    maior = terceiro
print('Maior valor digitado foi: {}' .format(maior))
menor = primeiro
if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro
print;('Menor valor digitado foi: {}' .format(menor))
