from abc import ABC, abstractmethod


class CRUD(ABC):    
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        m = 0
        for n in cls.objetos:
            if n.get_id() > m: m = n.get_id()
        obj.set_id(m + 1)
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
            if n.get_id == id: return n
        return None
    
    @classmethod
    def atualizar(cls, obj):
        n = cls.listar_id(obj.get_id)
        if n != None:
            cls.objetos.insert(cls.objetos.index(n), obj)
            cls.remove(n)
        cls.salvar()

    @classmethod
    def excluir(cls, obj):
        n = cls.listar_id(obj.get_id())
        if n != None:
            cls.objetos.remove(n)
        cls.salvar()

    @classmethod
    @abstractmethod
    def Abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def Salvar(cls):
        pass