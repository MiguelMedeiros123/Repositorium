import json
from models.crud import CRUD


class Servico:
    def __init__(self, id: int, descricao: str, valor: float, duracao: int):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
        self.set_duracao(duracao)
        
    def __str__(self):
        return f"{self.get_id()} - {self.get_descricao()} - ${self.get_valor()} - {self.get_duracao()}min"
    
    def to_json(self):
        dic = {}
        dic["id"] = self.get_id()
        dic["descricao"] = self.get_descricao()
        dic["valor"] = self.get_valor()
        dic["duracao"] = self.get_duracao()
        return dic
    
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    
    def set_descricao(self, descricao):
        if descricao == "": raise ValueError("Descrição inválida.")
        self.__descricao = descricao
    def get_descricao(self):
        return self.__descricao
    
    def set_valor(self, valor):
        if valor < 0: raise ValueError("Valor inválido.")
        self.__valor = valor
    def get_valor(self):
        return self.__valor
    
    def set_duracao(self, duracao):
        if duracao < 0: raise ValueError("Duração inválida.")
        self.__duracao = duracao
    def get_duracao(self):
        return self.__duracao

class Servicos(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("Agenda/dados/servicos.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Agenda/dados/servicos.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Servico.to_json)