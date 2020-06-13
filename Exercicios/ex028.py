import random
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ...')
jogador = int(input('Em que número eu pensei? '))
escolhido = random.randint(0,5)
print('Processando...')
if jogador == escolhido:
    print('PARABÉNS! Você conseguiu me vencer! ')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!' .format(escolhido,jogador))





