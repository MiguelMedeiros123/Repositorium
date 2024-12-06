import json
from models.crud import CRUD


class Perfil:
    def __init__(self, id: int, nome: str, descricao: str, beneficios: str):
        self.set_id(id)
        self.set_nome(nome)
        self.set_descricao(descricao)
        self.set_beneficios(beneficios)

    def __str__(self):
        return f"{self.get_id()} - {self.get_nome()} - {self.get_descricao()} - {self.get_beneficios()}"

    def to_json(self):
        dic = {}
        dic["id"] = self.get_id()
        dic["nome"] = self.get_nome()
        dic["descricao"] = self.get_descricao()
        dic["beneficios"] = self.get_beneficios()
        return dic

    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido.")
        self.__nome = nome
    def get_nome(self):
        return self.__nome
    
    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição inválida.")
        self.__descricao = descricao
    def get_descricao(self):
        return self.__descricao
    
    def set_beneficios(self, beneficios):
        if beneficios == "": raise ValueError("Beneficios inválidos.")
        self.__beneficios = beneficios
    def get_beneficios(self):
        return self.__beneficios
    
class Perfis(CRUD):
    @classmethod
    def salvar(cls):  
        with open("Agenda/dados/perfis.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Perfil.to_json) 

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("Agenda/dados/perfis.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Perfil(obj["id"], obj["nome"], obj["descricao"], obj["beneficios"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass