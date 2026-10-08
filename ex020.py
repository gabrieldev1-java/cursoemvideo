import random

a1 = str(input('Digite o nome do primeiro aluno: '))
a2 = str(input('Digite o nome do segundo aluno: '))
a3 = str(input('Digite o nome do terceiro aluno: '))
lista =  [a1, a2, a3]
random.shuffle(lista)
print('a ordem de apresentação será')
print(lista)