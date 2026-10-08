from random import randint
from time import sleep

cont = 0
lista = list()
jogos = list()
quant = int(input('Quantos jogos voce quer que eu sorteie?'))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        numero = randint(1, 60)
        if numero not in lista:
            lista.append(numero)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('-'*40)
for i , lista in enumerate(jogos):
    print(f'Jogo {i+1}: {lista}')
    sleep(1)
print('-'*40)