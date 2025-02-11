from abc import ABC, abstractmethod
import json
from models.empresas import Empresa
from models.setores import Setor
from models.funcionarios import Funcionario
import datetime as dt



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
            if n.get_id() == id: return n
        return None
    
    @classmethod
    def atualizar(cls, obj):
        n = cls.listar_id(obj.get_id())
        if n != None:
            cls.objetos.insert(cls.objetos.index(n), obj)
            cls.objetos.remove(n)
        cls.salvar()

    @classmethod
    def excluir(cls, obj):
        n = cls.listar_id(obj.get_id())
        if n != None:
            cls.objetos.remove(n)
            cls.salvar()

    @classmethod
    @abstractmethod
    def abrir(cls):
        pass

    @classmethod
    @abstractmethod
    def salvar(cls):
        pass



class Empresas(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Projeto.2/data/empresas.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    e = Empresa(obj["id"], obj["nome"], obj["desc"], obj["dono"], dt.datetime.strptime(obj["fund"], "%d/%m/%Y").date(), obj["setores"])
                    cls.objetos.append(e)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Projeto.2/data/empresas.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Empresa.to_json)



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