from random import randint
from time import sleep

computador = randint(1, 3)
print('''Suas Opções:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('qual é sua jogada?: '))
print('JO' )
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO!!!')
sleep(0.5)
print('-=' * 12)
print('Computador jogou {}'.format(computador))
print('Jogador jogou {}'.format(jogador))
print('-=' * 12)
if computador == 1:
    if jogador == 1:
        print('EMPATE!!')
    elif jogador == 2:
        print('JOGADOR VENCEU!!')
    elif jogador == 3:
        print('JOGADOR VENCEU!!')

if computador == 2:
    if jogador == 1:
        print('COMPUTADOR VENCEU!!')
    elif jogador == 2:
        print(' EMPATE!!')
    elif jogador == 3:
        print('JOGADOR VENCEU!!')

if computador == 3:
     if jogador == 1:
         print('COMPUTADOR VENCEU!!')
     elif jogador == 2:
         print('COMPUTADOR VENCEU!!')
     elif jogador == 3:
         print('EMPATE!!')
print('-=' * 12)
