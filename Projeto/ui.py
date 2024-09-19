import views
import datetime as dt

class UI:
    @staticmethod
    def menu():
        print("Cadastro de empresas: ")
        print("1 - inserir, 2 - listar, 3 - atualizar, 4 - excluir.")
        print("Cadastro de setores: ")
        print("5 - inserir setor, 6 - listar setores, 7 - atualizar setor, 8 - excluir setor.")
        print("Cadastro de funcionários: ")
        print("9 - inserir funcionário, 10 - listar funcionários, 11 - atualizar funcionário, 12 - excluir funcionário.")
        print("13 - Fim.")
        return int(input("Informe uma opção: "))
    
    @staticmethod
    def main():
        op = 0
        while op != 13:
            op = UI.menu()
            print()
            if op == 1: UI.empresa_inserir()
            if op == 2: UI.empresa_listar()
            if op == 3: UI.empresa_atualizar()
            if op == 4: UI.empresa_excluir()
            if op == 5: UI.setor_inserir()
            if op == 6: UI.setor_listar()
            if op == 7: UI.setor_atualizar()
            if op == 8: UI.setor_excluir()
            if op == 9: UI.funcionario_inserir()
            if op == 10: UI.funcionario_listar()
            if op == 11: UI.funcionario_atualizar()
            if op == 12: UI.funcionario_excluir()

    @staticmethod
    def empresa_inserir():
        nome = input("Informe o nome: ")
        desc = input("Informe a descrição: ")
        dono = input("Informe o dono: ")
        views.empresa_inserir(nome, desc, dono)
    
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
        views.empresa_atualizar(id, nome, desc, dono)
    
    @staticmethod
    def empresa_excluir():
        UI.empresa_listar()
        id = int(input("Informe o ID da empresa a excluir: "))
        views.empresa_excluir(id)

    @staticmethod
    def setor_inserir():
        nome = input("Informe o nome: ")
        desc = input("Informe a descrição: ")
        data = dt.datetime.strptime(input("Informe a data de fundação (formato dd/mm/aaaa): "), "%d/%m/%Y")
        views.setor_inserir(nome, desc, data)
    
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
        data = dt.datetime.strptime(input("Informe a nova data de fundação (formato dd/mm/aaaa): "), "%d/%m/%Y")
        views.setor_atualizar(id, nome, desc, data)
    
    @staticmethod
    def setor_excluir():
        UI.setor_listar()
        id = int(input("Informe o ID do setor a excluir: "))
        views.setor_excluir(id)

UI.main()