from datetime import date
ano = int(input('Qual ano você nasceu: '))
genero = str(input('Você é HOMEM ou MULHER? '))
atual = date.today().year
idade = atual - ano
alistamento = ano + 18
print('Quem nasceu em {} tem {} anos em {}.' .format(ano,idade, atual))
if genero == 'MULHER' or 'Mulher' 'mulher':
    print('Você \033[4mNÃO\033[m precisa se alistar!')
elif idade < 18:
    soma = 18 - idade
    print('Ainda Faltam {} anos para o alistamento.' .format(soma))
    print('Seu alistamento será {}.' .format(alistamento))
elif idade > 18:
    soma = idade - 18
    print('Você ja deveria ter se alistado há {} anos.' .format(soma))
    print('Seu alistamento foi em {}.' .format(alistamento))
elif ano == 18:
    print('Você tem que se alistar \033[4mIMEDIATAMENTE!!\033[m')

