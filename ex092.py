jogador = dict()
jogador['Nome'] = str(input('Nome: '))
tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou: '))
partidas = list()
for c in range(0, tot):
    go = int(input(f'Quantos gols na partida {c}: '))
    partidas.append(go)
jogador['Gols'] = partidas[:]
jogador['Totasl de Gols'] = sum(partidas)
print('-=' * 50)
print(jogador)
print('-=' * 50)
for k,v in jogador.items():
    print(f'{k}: {v}')
print('-=' * 50)
print(f'O Jogador {jogador["Nome"]} jogou {tot} partidas.')
for c in range(0, tot):
    print(f'Na partida {c}, fez {partidas[c]} gols.')
