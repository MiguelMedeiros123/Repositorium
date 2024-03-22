def um_aluno():
    nome = input('Digita teu nome:\n')
    matr = input('Digita tua matrícula:\n')
    
    ano = ''
    for x in range(0, 4):
        ano += matr[x]
    #ou: ano = matr[0:4]
 
    print(f'\nNome: {nome};\nMatrícula: {matr};\nAno de ingresso: {ano}.')

def dez_alunos():
    alumni = []
    matriculae = []
    annos = []

    for x in range(1, 11):
        nome = input(f'Nome {x}: ')
        matr = input(f'Matrícula {x}: ')

        alumni.append(nome)
        matriculae.append(matr)
        annos.append(matr[0:4])
        print('\n')
    
    
    for y in range(len(alumni)):
        print(f'Aluno {y+1}: {alumni[y]}')
        print(f'Matrícula {y+1}: {matriculae[y]}')
        print(f'Ano de ingresso: {annos[y]}\n')

dez_alunos()