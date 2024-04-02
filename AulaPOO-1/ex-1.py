class triangulo:
    def __init__(self):
        self.b = 0
        self.h = 0
    def calc_area(self):
        return (self.b * self.h * 1/2)

t = triangulo()

#t.b = float(input('Digita a base do triângulo'))
#t.h = float(input('Digita a altura do triângulo'))

k = t

k.b = 10  #muda a variável à qual ambos 't' e 'k' fazem referência
k.h = 20

z = triangulo() #cria-se outro objeto da classe triângulo

z.b = 20
z.h = 40

print(f'\nBase de T: {t.b} ; Altura de T: {t.h}')
print(f'Área de T: {t.calc_area()}\n')

print(f'Base de K: {k.b} ; Altura de K: {k.h}')
print(f'Área de K: {k.calc_area()}\n')

print(f'Base de Z: {z.b} ; Altura de Z: {z.h}')
print(f'Área de Z: {z.calc_area()}\n')
