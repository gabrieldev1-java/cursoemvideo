n = str(input('Digite uma frase: ')).strip()
nome = n.split()

print('Muito prazer em te conhecer!')
print('Seu Primeiro nome é {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))