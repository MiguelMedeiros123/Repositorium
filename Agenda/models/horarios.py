import json
import datetime as dt

class Horario:
    def __init__(self, id: int, data: dt.datetime, confirmado: bool, idCliente: int, idServico: int):
        self.id = id
        self.data = data
        self.confirmado = confirmado
        self.idCliente = idCliente
        self.idServico = idServico
    def __str__(self):
        return f"{self.id} - {dt.datetime.strftime(self.data, "%d/%m/%Y %H:%M")}"
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["data"] = dt.datetime.strftime(self.data, "%d/%m/%Y %H:%M")
        dic["confirmado"] = self.confirmado
        dic["idCliente"] = self.idCliente
        dic["idServico"] = self.idServico
        return dic

class Horarios:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for n in cls.objetos:
            if n.id > m: m = n.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for n in cls.objetos:
            if id == n.id: return n
        return None
    
    @classmethod
    def atualizar(cls, obj):
        n = cls.listar_id(obj.id)
        if n != None:
            n.data = obj.data
            n.confirmado = obj.confirmado
            n.idCliente = obj.idCliente
            n.idServico = obj.idServico
        cls.salvar()

    @classmethod
    def excluir(cls, obj):
        n = cls.listar_id(obj.id)
        if n != None:
            cls.objetos.remove(n)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Agenda/dados/horarios.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Horario(obj["id"], dt.datetime.strptime(obj["data"], "%d/%m/%Y %H:%M"), obj["confirmado"], obj["idCliente"], obj["idServico"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Agenda/dados/horarios.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Horario.to_json)