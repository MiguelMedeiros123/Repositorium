import json

class Cliente:
    def __init__(self, id: int, nome: str, email: str, fone: str, senha: str):
        self.id = id
        self.nome = nome
        self.email = email
        self.fone = fone
        self.senha = senha
    def __str__(self):
        return f"{self.id} - {self.nome} - {self.email} - Tel: {self.fone}"
    
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
            c.senha = obj.senha
        cls.salvar()  

    @classmethod
    def excluir(cls, obj: Cliente):
        c = cls.listar_id(obj.id)
        if c != None: 
            cls.objetos.remove(c)
            cls.salvar()  

    @classmethod
    def salvar(cls):  
        with open("Agenda/Dados/clientes.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = vars) 

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try: 
            with open("Agenda/Dados/clientes.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], obj["senha"])
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass