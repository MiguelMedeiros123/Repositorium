import views
import datetime as dt

class UI:
    @staticmethod
    def menu():
        print("\nCadastro de empresas: ")
        print("1 - inserir, 2 - listar, 3 - atualizar, 4 - excluir, 5 - dados detalhados.")
        print("Cadastro de setores: ")
        print("6 - inserir, 7 - listar, 8 - atualizar, 9 - excluir, 10 - dados detalhados, 11 - mover a uma empresa")
        print("Cadastro de funcionários: ")
        print("12 - inserir, 13 - listar, 14 - atualizar, 15 - excluir, 16 - mover a um setor.")
        print("17 - Fim.")
        return int(input("\nInforme uma opção: "))
    
    @staticmethod
    def main():
        op = 0
        while op != 17:
            op = UI.menu()
            print()
            if op == 1: UI.empresa_inserir()
            if op == 2: UI.empresa_listar()
            if op == 3: UI.empresa_atualizar()
            if op == 4: UI.empresa_excluir()
            if op == 5: UI.empresa_listar_id()
            if op == 6: UI.setor_inserir()
            if op == 7: UI.setor_listar()
            if op == 8: UI.setor_atualizar()
            if op == 9: UI.setor_excluir()
            if op == 10: UI.setor_listar_id()
            if op == 11: UI.setor_mover_empresa()
            if op == 12: UI.funcionario_inserir()
            if op == 13: UI.funcionario_listar()
            if op == 14: UI.funcionario_atualizar()
            if op == 15: UI.funcionario_excluir()
            if op == 16: UI.funcionario_mover_setor()


    @staticmethod
    def funcionario_inserir():
        nome = input("Informe o nome: ")
        ocup = input("Informe a ocupação: ")
        nasc = dt.datetime.strptime(input("Informe a data de nascimento (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
        cpf = int(input("Informe o CPF: "))
        email = input("Informe o e-mail: ")
        custo = float(input("Informe o custo mensal: "))
        contr = dt.datetime.strptime(input("Informe a data de contratação (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
        views.funcionario_inserir(nome, ocup, nasc, cpf, email, custo, contr)
        print()
    
    @staticmethod
    def funcionario_listar():
        for f in views.funcionario_listar():
            print(f)
        print()
    
    @staticmethod
    def funcionario_atualizar():
        UI.funcionario_listar()
        id = int(input("Informe o ID do funcionário a atualizar: "))
        nome = input("Informe o novo nome: ")
        ocup = input("Informe a nova ocupação: ")
        nasc = dt.datetime.strptime(input("Informe a nova data de nascimento (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
        cpf = int(input("Informe o novo CPF: "))
        email = input("Informe o novo email: ")
        custo = float(input("Informe o novo custo mensal: "))
        contr = dt.datetime.strptime(input("Informe a nova data de contratação (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
        views.funcionario_atualizar(id, nome, ocup, nasc, cpf, email, custo, contr)
        print()
    
    @staticmethod
    def funcionario_excluir():
        UI.funcionario_listar()
        id = int(input("Informe o ID do funcionário a excluir: "))
        views.funcionario_excluir(id)
        print()

    @staticmethod
    def funcionario_mover_setor():
        UI.funcionario_listar()
        id_func = int(input("ID do funcionário a mover: "))
        print()
        UI.setor_listar()
        id_setor = int(input("ID do setor ao qual mover-se-á o funcionario: "))
        views.funcionario_mover_setor(id_func, id_setor)


    @staticmethod
    def setor_inserir():
        nome = input("Informe o nome: ")
        desc = input("Informe a descrição: ")
        data = dt.datetime.strptime(input("Informe a data de fundação (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
        views.setor_inserir(nome, desc, data)
        print()
    
    @staticmethod
    def setor_listar():
        for s in views.setor_listar():
            print(s)
        print()
    
    @staticmethod
    def setor_atualizar():
        UI.setor_listar()
        id = int(input("Informe o ID do setor a atualizar: "))
        nome = input("Informe o novo nome: ")
        desc = input("Informe a nova descrição: ")
        data = dt.datetime.strptime(input("Informe a nova data de fundação (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
        views.setor_atualizar(id, nome, desc, data)
        print()
    
    @staticmethod
    def setor_excluir():
        UI.setor_listar()
        id = int(input("Informe o ID do setor a excluir: "))
        views.setor_excluir(id)
        print()

    @staticmethod
    def setor_listar_id():
        UI.setor_listar()
        id = int(input("\nID do setor a listar: "))
        print()
        print(views.setor_listar_id(id))
        print("\n   Funcionários:\n")
        for f in views.funcionario_listar_setor(id):
            print(f"   {f}")
        print()

    @staticmethod
    def setor_mover_empresa():
        UI.setor_listar()
        id_setor = int(input("ID do setor a mover: "))
        print()
        UI.empresa_listar()
        id_empresa = int(input("ID da empresa à qual mover-se-á o setor: "))
        views.setor_mover_empresa(id_setor, id_empresa)


    @staticmethod
    def empresa_inserir():
        nome = input("Informe o nome: ")
        desc = input("Informe a descrição: ")
        dono = input("Informe o dono: ")
        fund = dt.datetime.strptime(input("Informe a data de fundação (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
        views.empresa_inserir(nome, desc, dono, fund)
        print()
    
    @staticmethod
    def empresa_listar():
        for e in views.empresa_listar():
            print(e)
        print()
    
    @staticmethod
    def empresa_atualizar():
        UI.empresa_listar()
        id = int(input("Informe o ID da empresa a atualizar: "))
        nome = input("Informe o novo nome: ")
        desc = input("Informe a nova descrição: ")
        dono = input("Informe o novo dono: ")
        fund = dt.datetime.strptime(input("Informe a data de fundação (formato dd/mm/aaaa): "), "%d/%m/%Y").date()
        views.empresa_atualizar(id, nome, desc, dono, fund)
        print()
    
    @staticmethod
    def empresa_excluir():
        UI.empresa_listar()
        id = int(input("Informe o ID da empresa a excluir: "))
        views.empresa_excluir(id)
        print()
    
    @staticmethod
    def empresa_listar_id():
        UI.empresa_listar()
        id = int(input("ID da empresa a listar: "))
        print()
        print(views.empresa_listar_id(id))
        print("\n   Setores:\n")
        for s in views.setor_listar_empresa(id):
            print(f"   {s}")
            print("\n       Funcionários:\n")
            for f in views.funcionario_listar_setor(s.id):
                print(f"       {f}")
            print()


UI.main()