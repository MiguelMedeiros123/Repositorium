import json
import datetime as dt

class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - {self.fone}"
    
class Clientes:
    objetos = []

    @classmethod
    def inserir(cls, obj: Cliente):
        cls.abrir()
        m = 0
        for c in cls.objetos:
            if c.id > m: m = c.id
        obj.id = m + 1  
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls) -> list:
        cls.abrir()
        return cls.objetos
    
    @classmethod
    def listar_id(cls, id: int) -> Cliente:
        cls.abrir()
        for c in cls.objetos:
            if c.id == id: return c
        return None
 
    @classmethod
    def atualizar(cls, obj: Cliente):
        c = cls.listar_id(obj.id)
        if c != None:
            c.nome = obj.nome
            c.email = obj.email
            c.fone = obj.fone
        cls.salvar()  

    @classmethod
    def excluir(cls, obj: Cliente):
        c = cls.listar_id(obj.id)
        if c != None: 
            cls.objetos.remove(c)
            cls.salvar()  

    @classmethod
    def salvar(cls):  
        with open("Agenda/clientes.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars) 

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("Agenda/clientes.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass




class Horario:
    def __init__(self, id, d):
        self.id = id
        self.data = d
        self.confirmado = False
        self.idCliente = 0
        self.idServico = 0
    def __str__(self):
        return f"{self.id} - {self.data} - {self.confirmado} - {self.idCliente} - {self.idServico}"
  
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
            with open("Agenda/horarios.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Horario(obj["id"], obj["data"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Agenda/horarios.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars)




class Servico:
    def __init__(self, id: int, descricao: str, valor: float, duracao: int):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.duracao = duracao
    def __str__(self):
        return f"{self.id} - {self.descricao} - {self.valor} - {self.duracao}"

class Servicos:
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
            if n.id == id: return n
        return None
    
    @classmethod
    def atualizar(cls, obj):
        n = cls.listar_id(obj.id)
        if n != None:
            n.descricao = obj.descricao
            n.valor = obj.valor
            n.duracao = obj.duracao
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
            with open("Agenda/servicos.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Servico(obj["id"], obj["nome"], obj["email"], obj["fone"])                     # dicionário
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Agenda/servicos.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)