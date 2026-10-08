n = int(input('Digite um numero inteiro: '))
fato = n
f = 1
print('Calculando {}!'.format(n), end=' ')
while fato > 0:
    print('{} '.format(fato), end='')
    print('x ' if fato > 1 else '= ', end='')
    f *= fato
    fato -= 1

print('{}'.format(f), end=' ')
