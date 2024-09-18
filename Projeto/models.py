import json
import datetime as dt


class Funcionario:
    def __init__(self, id: int, nome: str, ocup: str, nasc: dt.datetime, cpf: str, email: str, custo: float, contr: dt.datetime, id_setor: int) -> None:
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
        return f"{self.id} - {self.nome} - {self.ocup}; Nascimento - {dt.datetime.strftime(self.nasc, "%d/%M/%Y")}; CPF - {self.cpf}; E-mail - {self.email}; Custo mensal - {self.custo}; Data de contratação: {dt.datetime.strftime(self.contr, "%d/%M/%Y")}; ID do setor: {self.id_setor}"
    
    def to_json(self):
        dic = {}


class Funcionarios:
    objetos = []

    @classmethod
    def inserir(cls, obj: Funcionario):
        cls.abrir()
        m = 0
        for f in cls.objetos:
            if f.id > m: m = f.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> Funcionario:
        cls.abrir()
        for f in cls.objetos:
            if id == f.id: return f
        return None

    @classmethod
    def atualizar(cls, obj: Funcionario):
        cls.abrir()
        f = cls.listar_id(obj.id)
        if f != None:
            f.id = id
            f.nome = obj.nome
            f.ocup = obj.ocup
            f.nasc = obj.nasc
            f.cpf = obj.cpf
            f.email = obj.email
            f.custo = obj.custo
            f.contr = obj.contr
            f.id_setor = obj.id_setor
        cls.salvar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        f = cls.listar_id(id)
        if f != None:
            cls.objetos.remove(f)
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


class Setores:
    objetos = []

    @classmethod
    def listar_id(cls, id: int) -> Setor:
        cls.abrir()
        for s in cls.objetos:
            if s.id == id: return s
        return None

    @classmethod
    def inserir_func(cls, id: int, id_func: int):
        cls.abrir()
        s = cls.listar_id(id)
        if s != None:
            f = Funcionarios.listar_id(id_func)
            if f != None:
                s.funcionarios.append(id_func)
                s.custo += f.custo
                cls.salvar()