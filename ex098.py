from time import sleep


def contador(i, f, p):
    print('-'*30)
    sleep(1)
    print(f'Contagem de {i} ate {f} em {p}')
    sleep(1.5)
    if p <0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont} ', end='')
            sleep(1)
            cont -= p
        print('FIM')

contador(1, 10, 1)
contador(10, 0, 2)
sleep(1)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(ini, fim, passo)