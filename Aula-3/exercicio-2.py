#fazer sem .split()#
def jeito1():
    nome = input('Digita teu nome completo:\n- ')

    m = ''
    i = 0

    while nome[i] != " ":
        i += 1
        m += nome[i-1]   

    print(f'Bem-vindo ao Python, {m}.')

def jeito2():
    nome = input('Digita teu nome completo:\n- ')

    i = 0

    while nome[i] != " ":
        i += 1
       
    m = nome[0:i]

    print(f'Bem-vindo ao Python, {m}.')

def jeito3():
    nome = input('Digita teu nome completo:\n- ')
    i = nome.index(' ')

    print(f'Bem vindo ao Python, {nome[0:i]}.')

jeito3()