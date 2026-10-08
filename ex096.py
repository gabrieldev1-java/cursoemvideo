l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A Área de um terreno {largura} x {comprimento} é de {a}m ')
area(l,c)