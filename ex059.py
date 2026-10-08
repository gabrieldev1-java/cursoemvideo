p1 = float(input('Digite o primeiro valor: '))
p2 = float(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:

        print('=-'*20)
        print('''        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos numeros
        [5] Sair do programa''')
        if opcao == 1:
            soma = p1 + p2
            print('a soma de {} e {} é igual a {}'.format(p1,p2, soma))
        elif opcao == 2:
            mult = p1 * p2
            print('{} x {} é igual a {:.2f} '.format(p1,p2,mult))
        elif opcao == 3:
            if p1 > p2:
                print('{} é maior que {}'.format(p1,p2))
            else:
                print('{} é maior que {}'.format(p2,p1))
        elif opcao == 4:
            print('Informe os numero de novo')
            p1 = float(input('Digite o primeiro valor: '))
            p2 = float(input('Digite o segundo valor: '))

        opcao = int(input('qual é sua opcao: '))



