time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols ele marcou na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
for i, j in enumerate(time):
    print(f'{i:>3} ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:
    busca = int(input('Mostrar dados de qual jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'Nao existe jogador {busca}!')
    else:
        print(f'Levantamento do jogador {time[busca]  ["nome"]}')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'  No jogo {i+1} fez {g} gols.')
    print(f'Um total de {time[busca] ["total"]} gols.')


    print('-=' * 30)
print('<< VOLTE SEMPRE >>')