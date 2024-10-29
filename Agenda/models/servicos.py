import json

class Servico:
    def __init__(self, id: int, descricao: str, valor: float, duracao: int):
        self.id = id
        self.descricao = descricao
        self.valor = valor
        self.duracao = duracao
    def __str__(self):
        return f"{self.id} - {self.descricao} - ${self.valor} - {self.duracao}min"

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
            with open("Agenda/dados/servicos.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Servico(obj["id"], obj["descricao"], obj["valor"], obj["duracao"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Agenda/dados/servicos.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default=vars)