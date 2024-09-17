import json
import datetime as dt


class Funcionario:
    def __init__(self, id: int, nome: str, nasc: dt.datetime, cpf: str, email: str, custo: float, contr: dt.datetime, id_setor: int) -> None:
        self.id = id
        self.nome = nome
        self.nasc = nasc
        self.cpf = cpf
        self.email = email
        self.custo = custo
        self.contr = contr
        self.id_setor = id_setor

    def __str__(self) -> str:
        return f"{self.id} - {self.nome}; Nascimento - {dt.datetime.strftime(self.nasc, "%d/%M/%Y")}; CPF - {self.cpf}; E-mail - {self.email}; Custo mensal - {self.custo}; Data de contratação: {dt.datetime.strftime(self.contr, "%d/%M/%Y")}; ID do setor: {self.id_setor}"
    
    def to_json(self):
        dic = {}


class Funcionarios:
    objetos = []

    @classmethod
    def inserir(cls, obj: Funcionario):
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
    def listar_id(cls, id: int):
        cls.abrir()
        for n in cls.objetos:
            if id == n.id: return n
        return None

    @classmethod
    def atualizar(cls, obj: Funcionario):
        cls.abrir()
        n = cls.listar_id(obj.id)
        if n != None:
            n.id = id
            n.nome = obj.nome
            n.nasc = obj.nasc
            n.cpf = obj.cpf
            n.email = obj.email
            n.custo = obj.custo
            n.contr = obj.contr
            n.id_setor = obj.id_setor
        cls.salvar()

    @classmethod
    def excluir(cls, obj: Funcionario):
        cls.abrir()
        n = cls.listar_id(obj.id)
        if n != None:
            cls.objetos.remove(n)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("objetos.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Funcionario(obj["id"], obj["nome"], obj["email"], dt.datetime.strptime(obj["nasc"], "%d/%m/%Y")adsadasfasdfdsjkfnsdjkfsdbjkhnfbhnjkafjbhkabhjkn)
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("objetos.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Funcionario.to_json)


class Setor:
    def __init__(self, id: int, nome: str, desc: str, data: dt.datetime) -> None:
        self.id = id
        self.nome = nome
        self.desc = desc
        self.data = data
        self.funcionarios = []
        self.custo = 0
    def __str__(self) -> str:
        return f"{self.id} - {self.nome}; {self.desc}; Criado a {self.data}; Funcionários - {len(self.funcionarios)}; Custo mensal - {self.custo}"
    def inserir_func(self, id_func: int):
        self.funcionarios.append(id_func)
        self.custo += Funcionarios.listar_id(id_func).custo
