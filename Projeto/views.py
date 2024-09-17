from models import Funcionario, Funcionarios
import datetime as dt

class views:
    @staticmethod
    def Funcionario_inserir():
    #id = int(input("Informe o id: "))
        nome = input("Informe o nome: ")
        nasc = dt.datetime.strptime(input("Informe a data de nascimento (formato dd/mm/aaaa): "), "%d/%M/%Y")
        cpf = input("Informe o CPF: ")
        email = input("Informe o e-mail: ")
        custo = input("Informe o custo mensal: ")
        contr = dt.datetime.strptime(input("Informe a data de contratação (formato dd/mm/aaaa): "), "%d/%M/%Y")
        views.setor_listar(kjjjjjjjjjjjjjj) #abahshdashdahjasdhjasbhjdashbj
        id_setor = int(input("Informe o ID do setor em que estará o funcionário: "))
        c = Funcionario(0, nome, nasc, cpf, email, custo, contr, id_setor)
        Funcionarios.inserir(c)

    @staticmethod
    def funcionario_listar():
        for c in Funcionarios.listar():
            print(c)

    @staticmethod
    def funcionario_atualizar():
        views.Funcionario_listar()
        id = int(input("Informe o ID do funcionário a ser atualizado: "))
        nome = input("Informe o novo nome: ")
        nasc = dt.datetime.strptime(input("Informe a nova data de nascimento (formato dd/mm/aaaa): "), "%d/%M/%Y")
        cpf = input("Informe o novo CPF: ")
        email = input("Informe o novo e-mail: ")
        custo = input("Informe o novo custo mensal: ")
        contr = dt.datetime.strptime(input("Informe a nova data de contratação (formato dd/mm/aaaa): "), "%d/%M/%Y")
        id_setor = int(input("Informe o ID do setor ao qual transferir-se-á o funcionário: "))
        c = Funcionario(id, nome, nasc, cpf, email, custo, contr, id_setor)
        Funcionarios.atualizar(c)

    @staticmethod
    def funcionario_excluir():
        views.Funcionario_listar()
        id = int(input("Informe o id do Funcionario a ser excluído: "))
        c = Funcionario(id, "", "", "", "", "", "", "")
        Funcionarios.excluir(c)