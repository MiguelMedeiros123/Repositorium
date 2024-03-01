print('Digita a base e a altura do retângulo:')
b = float(input('- '))
h = float(input('- '))

a = b*h
p = 2*(b+h)
d = (b**2 + h**2)**(1/2)

print(f'Área = {a} --- Perímetro = {p} --- Diagonal = {d}')