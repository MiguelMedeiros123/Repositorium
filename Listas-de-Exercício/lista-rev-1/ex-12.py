op = input('Digita dois valores inteiros separados por um operador +, -, * ou /\n')

n = op.split('+')
if len(n) == 2: print(f'O resultado da operação é {int(n[0]) + int(n[1])}')

else:
    n = op.split('-')
    if len(n) == 2: print(f'O resultado da operação é {int(n[0]) - int(n[1])}')

    else:
        n = op.split('*')
        if len(n) == 2: print(f'O resultado da operação é {int(n[0]) * int(n[1])}')

        else:
            n = op.split('/')
            if len(n) == 2: print(f'O resultado da operação é {int(n[0]) / int(n[1])}')

            else:
                print('Input errado.')