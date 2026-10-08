f = str(input('Digite uma frase: ')).strip()
print('a letra A apareceu {} vezes'.format(f.count('a')))
print('a letra A apareceu na posição {}'.format(f.find('a')+1))
print('a ultima letra A apareceu na posição {}'.format(f.rfind('a')+1))