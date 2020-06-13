a = float(input('Primeira Nota: '))
b = float(input('Segunda Nota: '))
media = (a + b) / 2
print(' Quem tirou {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(a,b,media))
if media < 5:
    print('O Aluno está REPROVADO')
elif media > 5 and media <7:
    print('O Aluno está RECUPERAÇÃO')
elif media >= 7 :
    print(' O Aluno está APROVADO')
