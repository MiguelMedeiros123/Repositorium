import json
import datetime as dt
from models.crud import CRUD
from models.setores import Setores


class Funcionario:
    def __init__(self, id: int, nome: str, ocup: str, nasc: dt.date, cpf: int, email: str, custo: float, contr: dt.date, id_setor: int) -> None:
        self.id = id
        self.nome = nome
        self.ocup = ocup
        self.nasc = nasc
        self.cpf = cpf
        self.email = email
        self.custo = custo
        self.contr = contr
        self.id_setor = id_setor

    def __str__(self) -> str:
        return f"{self.id} - {self.nome} - {self.ocup}; Nascimento - {dt.date.strftime(self.nasc, '%d/%m/%Y')}; CPF - {self.cpf}; E-mail - {self.email}; Custo mensal - {self.custo}; Data de contratação: {dt.date.strftime(self.contr, '%d/%m/%Y')}; ID do setor: {self.id_setor}; ID da empresa: {self.id_empresa()}"
    
    def id_empresa(self) -> int:
        if Setores.listar_id(self.id_setor) == None: return 0
        else: return Setores.listar_id(self.id_setor).id_empresa

    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["ocup"] = self.ocup
        dic["nasc"] = dt.date.strftime(self.nasc, "%d/%m/%Y")
        dic["cpf"] = self.cpf
        dic["email"] = self.email
        dic["custo"] = self.custo
        dic["contr"] = dt.date.strftime(self.contr, "%d/%m/%Y")
        dic["id_setor"] = self.id_setor
        return dic


class Funcionarios(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Projeto.2/data/funcionarios.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    f = Funcionario(obj["id"], obj["nome"], obj["ocup"], dt.datetime.strptime(obj["nasc"], "%d/%m/%Y").date(), obj["cpf"], obj["email"], obj["custo"], dt.datetime.strptime(obj["contr"], "%d/%m/%Y"), obj["id_setor"])
                    cls.objetos.append(f)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Projeto.2/data/funcionarios.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Funcionario.to_json)