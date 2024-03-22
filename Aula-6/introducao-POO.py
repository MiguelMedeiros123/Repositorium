class alumnus:
    def __init__(self):
        self.nome = ''    #construtor
        self.matr = ''    #atributo
    
    def ano(self):        #método
        return int(self.matr[0:4])

aluno = alumnus()

aluno.nome = input('Digita teu nome:\n')
aluno.matr = input('Digita tua matrícula:\n')

print(f"\n{aluno.nome}, {aluno.matr}, {aluno.ano()}")