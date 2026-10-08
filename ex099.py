from time import sleep


def maior(*num):
    cont = maior = 0
    sleep(1)
    print('-'*40)
    sleep(1)
    print('\nAnalisando os valores passados...')
    for valor in num:
        print(f'{valor} ', end='')
        sleep(1)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    sleep(1)
    print(f'- Foram informados {cont} valores ao todo')
    sleep(1)
    print(f'O maior valor informado foi {maior}')





# programa Principal
maior(2,9,4,5,7,0)
maior(2,3,6,8,2,11)
maior()