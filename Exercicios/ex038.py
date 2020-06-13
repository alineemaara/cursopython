a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
if a>b:
    print('O \033[1;33;45mPRIMEIRO\033[m valor é o maior.')
elif b>a:
    print('O \033[1;33;45mSEGUNDO\033[m valor é o maior.')
elif a == b:
    print('Os dois valores são \033[1;33;45mIGUAIS\033[m!')
