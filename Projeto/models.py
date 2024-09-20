import json
import datetime as dt


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
        cls.salvar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        f = cls.listar_id(id)
        if f != None:
            cls.objetos.remove(f)
            cls.salvar()

    @classmethod
    def mover_setor(cls, id_func: int, id_setor: int):
        cls.abrir()
        f = cls.listar_id(id_func)
        if f != None:
            Setores.abrir()
            s1 = Setores.listar_id(f.id_setor)
            if s1 != None:
                s1.funcionarios -= 1
                Setores.salvar()
            s2 = Setores.listar_id(id_setor)
            if s2 != None:
                s2.funcionarios += 1
                f.id_setor = id_setor
                Setores.salvar()
            else: f.id_setor = 0
        cls.salvar()

    @classmethod
    def listar_setor(cls, id_setor) -> list:
        Setores.abrir()
        s = Setores.listar_id(id_setor)
        if s!= None:
            cls.abrir()
            l = []
            for f in cls.listar():
                if f.id_setor == id_setor:
                    l.append(f)
            return l
        return []
    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("funcionarios.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    f = Funcionario(obj["id"], obj["nome"], obj["ocup"], dt.datetime.strptime(obj["nasc"], "%d/%m/%Y").date(), obj["cpf"], obj["email"], obj["custo"], dt.datetime.strptime(obj["contr"], "%d/%m/%Y"), obj["id_setor"])
                    cls.objetos.append(f)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("funcionarios.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Funcionario.to_json)


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


class Setores:
    objetos = []
    
    @classmethod
    def inserir(cls, obj: Setor):
        cls.abrir()
        m = 0
        for s in cls.objetos:
            if s.id > m: m = s.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list:
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
    def excluir(cls, id: int):
        cls.abrir()
        s = cls.listar_id(id)
        if s != None:
            cls.objetos.remove(s)
            cls.salvar()

    @classmethod
    def mover_empresa(cls, id_setor: int, id_empresa: int):
        cls.abrir()
        s = cls.listar_id(id_setor)
        if s != None:
            Empresas.abrir()
            e1 = Empresas.listar_id(s.id_empresa)
            if e1 != None:
                e1.setores -= 1
                Empresas.salvar()
            e2 = Empresas.listar_id(id_empresa)
            if e2 != None:
                e2.setores += 1
                s.id_empresa = id_empresa
                Empresas.salvar()
            else: s.id_empresa = 0
        cls.salvar()

    @classmethod
    def listar_empresa(cls, id_empresa: int) -> list:
        Empresas.abrir()
        e = Empresas.listar_id(id_empresa)
        if e!= None:
            cls.abrir()
            l = []
            for s in cls.listar():
                if s.id_empresa == id_empresa:
                    l.append(s)
            return l
        return []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("setores.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Setor(obj["id"], obj["nome"], obj["desc"], dt.datetime.strptime(obj["data"], "%d/%m/%Y").date(), obj["funcionarios"], obj["id_empresa"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("setores.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Setor.to_json)


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

class Empresas:
    objetos = []

    @classmethod
    def inserir(cls, obj: Empresa):
        cls.abrir()
        m = 0
        for e in cls.objetos:
            if e.id > m: m = e.id
        obj.id = m + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id: int) -> Empresa:
        cls.abrir()
        for e in cls.objetos:
            if id == e.id: return e
        return None

    @classmethod
    def atualizar(cls, obj: Empresa):
        cls.abrir()
        e = cls.listar_id(obj.id)
        if e != None:
            e.nome = obj.nome
            e.desc = obj.desc
            e.dono = obj.dono
            e.fund = obj.fund
        cls.salvar()

    @classmethod
    def excluir(cls, id):
        cls.abrir()
        e = cls.listar_id(id)
        if e != None:
            cls.objetos.remove(e)
            cls.salvar()

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("empresas.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    e = Empresa(obj["id"], obj["nome"], obj["desc"], obj["dono"], dt.datetime.strptime(obj["fund"], "%d/%m/%Y").date(), obj["setores"])
                    cls.objetos.append(e)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("empresas.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Empresa.to_json)