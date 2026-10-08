from time import sleep
from random import randint

 
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        n = randint(0, 10)
        lista.append(n)
        print(f'{n}', end=' ')
        sleep(0.5)
    print('PRONTO!')


def somar( lista ):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos numeros para {lista} é de {soma}')


numeros = list()
sorteia(numeros)
somar(numeros)
