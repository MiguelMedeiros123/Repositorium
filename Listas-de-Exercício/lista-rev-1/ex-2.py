print('Digite quatro valores inteiros')
a = int(input())
b = int(input())
c = int(input())
d = int(input())

m = (a+b+c+d)/4

print(f'\nMédia = {m}')
print('Números menores que a média')
if a < m: print(a)
if b < m: print(b)
if c < m: print(c)
if d < m: print(d)

print('Números maiores ou iguais à média')
if a >= m: print(a)
if b >= m: print(b)
if c >= m: print(c)
if d >= m: print(d)