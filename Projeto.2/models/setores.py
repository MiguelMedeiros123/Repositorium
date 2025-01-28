import json
import datetime as dt
from models.crud import CRUD
from models.funcionarios import Funcionarios


class Setor:
    def __init__(self, id: int, nome: str, desc: str, data: dt.date, funcionarios: int, id_empresa: int) -> None:
        self.id = id
        self.nome = nome
        self.desc = desc
        self.data = data
        self.funcionarios = funcionarios
        self.id_empresa = id_empresa

    def __str__(self) -> str:
        return f"{self.id} - {self.nome}; {self.desc}; Criado a {dt.date.strftime(self.data, '%d/%m/%Y')}; N.º de funcionários - {self.funcionarios}; Gasto mensal - {self.custo()}; ID da empresa - {self.id_empresa}"
    
    def custo(self) -> float:
        custo = 0
        for f in Funcionarios.listar():
            if f.id_setor == self.id: custo += f.custo
        return custo

    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["desc"] = self.desc
        dic["data"] = dt.date.strftime(self.data, "%d/%m/%Y")
        dic["funcionarios"] = self.funcionarios
        dic["id_empresa"] = self.id_empresa
        return dic


class Setores(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Projeto.2/data/setores.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Setor(obj["id"], obj["nome"], obj["desc"], dt.datetime.strptime(obj["data"], "%d/%m/%Y").date(), obj["funcionarios"], obj["id_empresa"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Projeto/setores.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Setor.to_json)
