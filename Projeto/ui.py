import views
import datetime as dt

class UI:
    @staticmethod
    def menu():
        print("Cadastro de empresas: ")
        print("1 - inserir, 2 - listar, 3 - atualizar, 4 - excluir, 5 - listar especificamente.")
        print("Cadastro de setores: ")
        print("6 - inserir, 7 - listar, 8 - atualizar, 9 - excluir, 10 - listar especificamente, 11 - mover a uma empresa")
        print("Cadastro de funcionários: ")
        print("12 - inserir, 13 - listar, 14 - atualizar, 15 - excluir, 16 - inserir em setor.")
        print("17 - Fim.")
        return int(input("Informe uma opção: "))
    
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
            if op == 12: UI.funcionario_inserir
            if op == 13: UI.funcionario_listar()
            if op == 14: UI.funcionario_atualizar()
            if op == 15: UI.funcionario_excluir()
            if op == 16: UI.funcionario_mover_setor()

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
    def empresa_listar_id():
        UI.empresa_listar()
        id = int(input("ID da empresa a listar: "))
        aasdasdsa

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