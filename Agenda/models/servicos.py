import json
from crud import CRUD


class Servico:
    def __init__(self, id: int, descricao: str, valor: float, duracao: int):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)
        self.set_duracao(duracao)
        
    def __str__(self):
        return f"{self.get_id()} - {self.get_descricao()} - ${self.get_valor()} - {self.get_duracao()}min"

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
            json.dump(cls.objetos, arquivo, default=vars)