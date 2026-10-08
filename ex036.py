casa = float(input('valor da casa: R$ '))
salario = float(input('seu salario: R$ '))
anos = int(input('quantos anos deseja pagar: '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print('para pagar uma casa de {:.2f} em {} Anos'.format(casa, anos), end='')
print('a prestação sera de {:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Emprestimo aprovado')
else:
    print('Emprestimo Negado')