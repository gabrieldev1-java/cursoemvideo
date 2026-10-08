from random import randint
computador = randint(0,10)
print('sou seu computador...')
print('Vou pensar em um numero entre 0 e 10.')
print('consegue adivinhar...')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Em que numero eu pensei? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('mais... Tente mais uma vez')
        elif jogador > computador:
            print('menos... Tente mais uma vez')
print('eu pensei em {} e voce pensou em {}. PARABENS acertou com {} Tentativas'.format(computador,jogador,palpite))