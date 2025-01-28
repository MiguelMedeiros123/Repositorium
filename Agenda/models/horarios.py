import json
import datetime as dt
from models.crud import CRUD


class Horario:
    def __init__(self, id: int, data: dt.datetime, confirmado: bool, idCliente: int, idServico: int, idProfissional: int):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(confirmado)
        self.set_idCliente(idCliente)
        self.set_idServico(idServico)
        self.set_idProfissional(idProfissional)

    def __str__(self):
        return f"{self.get_id()} - {dt.datetime.strftime(self.get_data(), '%d/%m/%Y %H:%M')}"
    
    def to_json(self):
        dic = {}
        dic["id"] = self.get_id()
        dic["data"] = dt.datetime.strftime(self.get_data(), "%d/%m/%Y %H:%M")
        dic["confirmado"] = self.get_confirmado()
        dic["idCliente"] = self.get_idCliente()
        dic["idServico"] = self.get_idServico()
        dic["idProfissional"] = self.get_idProfissional()
        return dic
    
    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id
    
    def set_data(self, data):
        self.__data = data
    def get_data(self) -> dt.datetime:
        return self.__data
    
    def set_confirmado(self, confirmado):
        self.__confirmado = confirmado
    def get_confirmado(self):
        return self.__confirmado
    
    def set_idCliente(self, idCliente):
        self.__idCliente = idCliente
    def get_idCliente(self):
        return self.__idCliente
    
    def set_idServico(self, idServico):
        self.__idServico = idServico
    def get_idServico(self):
        return self.__idServico
    
    def set_idProfissional(self, idProfissional):
        self.__idProfissional = idProfissional
    def get_idProfissional(self):
        return self.__idProfissional

class Horarios(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Agenda/dados/horarios.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Horario(obj["id"], dt.datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"), obj["confirmado"], obj["idCliente"], obj["idServico"], obj["idProfissional"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Agenda/dados/horarios.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Horario.to_json)