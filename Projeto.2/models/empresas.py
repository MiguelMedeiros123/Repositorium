import json
import datetime as dt
from models.crud import CRUD
from models.setores import Setores


class Empresa:
    def __init__(self, id: int, nome: str, desc: str, dono: str, fund: dt.date, setores: int):
        self.id = id
        self.nome = nome
        self.desc = desc
        self.dono = dono
        self.fund = fund
        self.setores = setores
    
    def custo(self) -> float:
        custo = 0
        for s in Setores.listar():
            if s.id_empresa == self.id: custo += s.custo()
        return custo
        
    def __str__(self) -> str:
        return f"{self.id} - {self.nome}; {self.desc}; Dono - {self.dono}; Fundada a {dt.date.strftime(self.fund, '%d/%m/%Y')}; N.º de setores: {self.setores}; Gasto mensal: {self.custo()}"

    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["desc"] = self.desc
        dic["dono"] = self.dono
        dic["fund"] = dt.date.strftime(self.fund, "%d/%m/%Y")
        dic["setores"] = self.setores
        return dic

class Empresas(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Projeto.2/data/empresas.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    e = Empresa(obj["id"], obj["nome"], obj["desc"], obj["dono"], dt.datetime.strptime(obj["fund"], "%d/%m/%Y").date(), obj["setores"])
                    cls.objetos.append(e)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Projeto.2/data/empresas.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Empresa.to_json)