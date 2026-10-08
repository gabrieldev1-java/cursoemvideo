times = ('flamengo', 'palmeiras', 'atletico paranaense' , 'Fluminense',
        'Bahia', 'Cruzeiro', 'Atletico-MG',
         'Santos', 'Coritiba', 'RB Bragantino')

print('-='*70)
print(f'Times do Brasileirão: {times}')
print('-='*70)
print(f'Os 5 primeiros colocados: {times[0:5]}')
print('-='*70)
print(f'Os 4 ultimos colocados: {times[-4:]}')
print('-='*70)
print(f'Os times em ordem alfabetica: {sorted(times)}')
print('-='*70)
print(f'O ultimo colocado é o RB Bragantino e sua posição na tabela é {times.index('RB Bragantino') +1}')
print('-='*70)  
