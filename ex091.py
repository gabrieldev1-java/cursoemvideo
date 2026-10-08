from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados ['idade'] = datetime.now().year - nascimento
dados['ctps'] = int(input('Carteira de trabalho: '))
if dados['ctps'] != 0:
    dados['contratacao'] = int(input('ano de contratacao:'))
    dados['salario'] = float(input('Salario: R$'))
    dados['aposentadoria'] = dados['idade']  + ((dados['contratacao'] + 35) - datetime.now().year)

for k,v in dados.items():
    print(f'{k}: {v}')