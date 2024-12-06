import json
from models.crud import CRUD


class Profissional:
    def __init__(self, id: int, nome: str, especialidade: str, conselho: str, email: str, senha: str):
        self.set_id(id)
        self.set_nome(nome)
        self.set_especialidade(especialidade)
        self.set_conselho(conselho)
        self.set_email(email)
        self.set_senha(senha)

    def __str__(self):
        return f"{self.get_id()} - {self.get_nome()} - {self.get_especialidade()} - {self.get_conselho()} - {self.get_email()}"

    def to_json(self):
        dic = {}
        dic["id"] = self.get_id()
        dic["nome"] = self.get_nome()
        dic["especialidade"] = self.get_especialidade()
        dic["conselho"] = self.get_conselho()
        dic["email"] = self.get_email()
        dic["senha"] = self.get_senha()
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
    
    def set_especialidade(self, especialidade):
        if especialidade == "": raise ValueError("Especialidade inválida.")
        self.__especialidade = especialidade
    def get_especialidade(self):
        return self.__especialidade
    
    def set_conselho(self, conselho):
        if conselho == "": raise ValueError("Conselho inválido.")
        self.__conselho = conselho
    def get_conselho(self):
        return self.__conselho
    
    def set_email(self, email):
        if email == "": raise ValueError("E-mail inválido.")
        self.__email = email
    def get_email(self):
        return self.__email
    
    def set_senha(self, senha):
        if senha == "": raise ValueError("Senha inválida.")
        self.__senha = senha
    def get_senha(self):
        return self.__senha
    
class Profissionais(CRUD):
    @classmethod
    def salvar(cls):  
        with open("Agenda/dados/profissionais.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Profissional.to_json) 

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("Agenda/dados/profissionais.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Profissional(obj["id"], obj["nome"], obj["especialidade"], obj["conselho"], obj["email"], obj["senha"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass