print('Digite três valores:')
a = float(input())
b = float(input())
c = float(input())

if a == b and b == c:
    print('Estes valores formam um triângulo equilátero.')

elif (a+b) > c and (a+c) > b and (b+c) > a:
    if a == b or a == c or b == c:
        print('Estes valores formam um triângulo isóceles.')
    else:
        print('Estes valores formam um triângulo escaleno.')

else: print('Esses valores não formam um triângulo')