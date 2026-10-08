aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno["Nome"]}:'))
if aluno['media'] >= 7:
    print('Aprovado')
else:
    print('Reprovado')
                                          

for k,v in aluno.items():
    print(f'{k}: {v}')
