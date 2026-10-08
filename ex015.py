d = int(input('Quantos dias voce ficou com o carro?'))
k = float(input('Quantos km rodar o carro?'))

a = (60 * d) + (k * 0.15)

print('O total a pagar R${:.2f}'.format(a))