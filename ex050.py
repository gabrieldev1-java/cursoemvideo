soma = 0
cont = 0

for c in range(1, 7 ):
    n = int(input('Digite um numero inteiro:'))
    if n % 2 == 0:
        soma += n
        cont += 1
print('voce informou {} numeros e a soma dos pares = {}'.format(n, soma))