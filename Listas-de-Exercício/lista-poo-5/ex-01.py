import datetime as dt
class Paciente:
    def __init__(self, n: str, c: str, t: str, nasc: dt) -> None:
        if n != "": self.__nome = n
        else: raise ValueError('Insere um nome válido')
        if c != "": self.__cpf = c
        else: raise ValueError('Insere um CPF válido')
        if t != "": self.__tel = t
        else: raise ValueError('Insere um telefone válido')
        if nasc <= dt.datetime.now(): self.__nasc = nasc
        else: raise ValueError('Insere uma data de nascimento válida')
    def Idade(self):
        i = dt.datetime.now() - self.__nasc
        a = i.days//365
        m = (i.days - 365*a)//30
        return f'{a} anos e {m} meses'
    def __str__(self):
        return f"Nome = {self.__nome}; CPF = {self.__cpf}; Telefone = {self.__tel}; Nascimento: {self.__nasc.strftime('%d/%m/%Y')}; Idade: {self.Idade()}"

n = input('Insere seu nome: ')
c = input('Insere seu CPF: ')
t = input('Insere seu telefone: ')
nasc = input('Insere sua data de nascimento (mm/dd/aaaa): ')

p = Paciente(n, c, t, dt.datetime.strptime(nasc, "%d/%m/%Y"))
print(p)