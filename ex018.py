import math

n = float(input('digite um numero real: '))
s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))
print('o seno de {}  é de {:.2f}'.format(n, s))
print('o coseno de {}  é de {:.2f}'.format(n, c))
print('a tangente de {}  é de {:.2f}'.format(n, t))