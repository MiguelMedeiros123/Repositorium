import json
from models.crud import CRUD


class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str, senha: str, idPerfil: int):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
        self.set_idPerfil(idPerfil)

    def __str__(self):
        return f"{self.get_id()} - {self.get_nome()} - {self.get_email()} - Tel: {self.get_fone()} - idPerfil: {self.get_idPerfil()}"

    def to_json(self):
        dic = {}
        dic["id"] = self.get_id()
        dic["nome"] = self.get_nome()
        dic["email"] = self.get_email()
        dic["fone"] = self.get_fone()
        dic["senha"] = self.get_senha()
        dic["idPerfil"] = self.get_idPerfil()
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
    
    def set_email(self, email):
        if email == "": raise ValueError("E-mail inválido.")
        self.__email = email
    def get_email(self):
        return self.__email
    
    def set_fone(self, fone):
        if fone == "": raise ValueError("Telefone inválido.")
        self.__fone = fone
    def get_fone(self):
        return self.__fone
    
    def set_senha(self, senha):
        if senha == "": raise ValueError("Senha inválida.")
        self.__senha = senha
    def get_senha(self):
        return self.__senha
    
    def set_idPerfil(self, idPerfil):
        self.__idPerfil = idPerfil
    def get_idPerfil(self):
        return self.__idPerfil
    
class Clientes(CRUD):
    @classmethod
    def salvar(cls):  
        with open("Agenda/dados/clientes.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Cliente.to_json) 

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("Agenda/dados/clientes.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"], obj["idPerfil"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass