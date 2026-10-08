import random

a1 = str(input('digite algo:'))
a2 = str(input('digite algo:'))
a3 = str(input('digite algo:'))
a4 = str(input('digite algo:'))
a5 = str(input('digite algo:'))
a6 = str(input('digite algo:'))
a7 = str(input('digite algo:'))
a8 = str(input('digite algo:'))
a9 = str(input('digite algo:'))
a10 = str(input('digite algo:'))

lista = [a1, a2, a3, a4, a5, a6, a7, a8, a9, a10]
escolhido = random.choice(lista)

print('o Aluno escolhido foi {}'.format(escolhido))


