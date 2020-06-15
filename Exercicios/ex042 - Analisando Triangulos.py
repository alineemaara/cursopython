n1= float(input('Primeiro Segmento: '))
n2= float(input('Segundo Segmento: '))
n3= float(input('Terceiro Segmento: '))
if n1+n2>n3 and n2+n3>n1 and n1+n3>n2:
    print('Os segmentos a cima PODEM FORMAR um triângulo ',end='')
    if n1 == n2 == n3:
        print('EQUILATERO')
    elif n1 != n2 != n3 != n1:
            print('ESCALENO')
    else:
            print('ISOSCELES')

else:
    print('Os segmentos a cima NÃO FORMAM um triângulo!')
