n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é {}' .format(nome[0]))
print('O seu ultimo nome é {}' .format(nome[len(nome)-1]))


