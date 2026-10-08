from datetime import datetime
dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['nascmento'] = int(input('Ano: '))
dados['Idade'] = datetime.now().year - dados['nascmento']
dados['ctps'] = int(input('CTPS: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Contratacao: '))
    dados['salario'] = float(input('Salario: '))
    dados['aposentadoria'] = dados['Idade'] + ((dados['contratacao'] + 35) - datetime.now().year)
for k,v in dados.items():
    print(f'{k}: {v}')