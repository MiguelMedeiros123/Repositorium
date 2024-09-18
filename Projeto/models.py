import json
import datetime as dt


class Funcionario:
    def __init__(self, id: int, nome: str, ocup: str, nasc: dt.date, cpf: str, email: str, custo: float, contr: dt.date, id_setor: int) -> None:
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
        return f"{self.id} - {self.nome} - {self.ocup}; Nascimento - {dt.date.strftime(self.nasc, "%d/%m/%Y")}; CPF - {self.cpf}; E-mail - {self.email}; Custo mensal - {self.custo}; Data de contratação: {dt.date.strftime(self.contr, "%d/%m/%Y")}; ID do setor: {self.id_setor}"
    
    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["ocup"] = self.ocup
        dic["nasc"] = dt.datetime.strftime(self.nasc, "%d/%m/%Y")
        dic["cpf"] = self.cpf
        dic["email"] = self.email
        dic["custo"] = self.custo
        dic["contr"] = dt.datetime.strftime(self.contr, "%d/%m/%Y")
        dic["id_setor"] = self.id_setor
        return dic


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
            with open("funcionarios.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Funcionario(obj["id"], obj["nome"], obj["email"], dt.date.strptime(obj["nasc"], "%d/%m/%Y")adsadasfasdfdsjkfnsdjkfsdbjkhnfbhnjkafjbhkabhjkn)
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("funcionarios.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Funcionario.to_json)


class Setor:
    def __init__(self, id: int, nome: str, desc: str, data: dt.date) -> None:
        self.id = id
        self.nome = nome
        self.desc = desc
        self.data = data
        self.funcionarios = []
        self.custo = 0

    def __str__(self) -> str:
        return f"{self.id} - {self.nome}; {self.desc}; Criado a {self.data}; Funcionários - {len(self.funcionarios)}; Custo mensal - {self.custo}"
    
    def to_json(self):
        dic = {}


class Setores:
    objetos = []
    
    @classmethod
    def inserir(cls, obj: Setor):
        cls.abrir()
        m = 0
        for s in cls.objetos:
            if s.id > m: m = s.id
        obj.id = m
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> Setor:
        cls.abrir()
        for s in cls.objetos:
            if s.id == id: return s
        return None
    
    @classmethod
    def atualizar(cls, obj: Setor):
        cls.abrir()
        s = cls.listar_id(obj.id)
        if s != None:
            s.nome = obj.nome
            s.desc = obj.desc
            s.data = obj.data
        cls.salvar()
    
    @classmethod
    def excluir(cls, id):
        cls.abrir()
        s = cls.listar_id(id)
        if s != None:
            cls.objetos.remove(s)
            cls.salvar()

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
    
    @classmethod
    def excluir_func(cls, id: int, id_func: int):
        cls.abrir()
        s = cls.listar_id(id)
        if s != None:
            f = Funcionarios.listar_id(id_func)
            if f.id in s.funcionarios:
                s.funcionarios.remove(f.id)
                s.custo -= f.custo
                cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("funcionarios.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Setor(obj["id"], obj["nome"], obj["email"], dt.date.strptime(obj["nasc"], "%d/%m/%Y")adsadasfasdfdsjkfnsdjkfsdbjkhnfbhnjkafjbhkabhjkn)
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("setores.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Setor.to_json)
