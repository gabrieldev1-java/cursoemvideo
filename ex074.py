from random import randint
n = randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10)
print(f'Os valores sorteados foram: ', end='')
for c in n:
    print(f'{c} ', end='')
print(f'\nO maior valor sorteado foi: {max(n)}', end='')
