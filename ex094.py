galera = list()
pessoas = dict()
soma = media = 0

while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo [Masculino/Feminino]: ')).strip().upper()
        if pessoas['sexo'] in ('M', 'MASCULINO'):
            pessoas['sexo'] = 'Masculino'
            break
        elif pessoas['sexo'] in ('F', 'FEMININO'):
            pessoas['sexo'] = 'Feminino'
            break
        print('ERRO! SOMENTE SEXO: MASCULINO OU FEMININO')
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    galera.append(pessoas.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()
        if resp in ('S', 'SIM', 'N', 'NAO'):
            break
        print('ERRO! Responda apenas S ou N.')
    if resp in ('N', 'NAO'):
        break
print('-=' * 30)
print(galera)
print('-=' * 30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas.')
media = soma / len(galera)
print(f'A media de idade é de {media:5.2f} anos.')
print('As mulheres cadastradas foram: ', end='')
for p in galera:
    if p['sexo'] == 'Feminino':
        print('    ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
            print()
print()
print('Lista de pessoas que estao acima da media:')
for p in galera:
    if p['idade'] >= media:
        print('   ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end=' ')
            print()
print('ENCERRADO!')
print('-=' * 30)
