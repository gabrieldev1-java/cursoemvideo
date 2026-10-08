temp = []
prin = []
mai = 0
men = 0
while True:
    temp.append( str(input('Digite um nome: ')))
    temp.append( float(input('Digite um peso: ')))
    if len(prin) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
             men = temp[1]
    prin.append( temp[:] )
    temp.clear()

    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    if resposta == 'N':
        break
print(f'Os dado foram {prin}')
print(f'Foram cadastradas {len(prin)} pessoas.')
print(f'O maior peso foi de {mai}. peso de ', end='')
for p in prin:
    if p[1] == mai:
        print(f'[{p[0]}] ... ', end='')
print()
print(f'O menor peso foi de {men}. peso de ', end='')
for p in prin:
    if p[1] == men:
        print(f'{p[0]} ... ', end='')
print()