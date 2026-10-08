from random import randint
computador  = randint(0 , 5)
print('-=-' * 20)
print('vou pensar em um numero entre 0 e 5 tente adivinhar')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei? '))

if jogador == computador:
    print('PARABÉNS VOCE ACERTOU')
else:
    print('errou, Voce pensou no numero {}'.format(jogador))