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
    def mover_setor(cls, id_empresa: int, id_setor: int):
        ef = cls.listar_id(id_empresa)
        s = Setores.listar_id(id_setor)
        if s != None:
            ei = cls.listar_id(s.get_id_empresa())
            if ei == None:
                if ef != None:
                    ef.set_setores(ef.get_setores()+1)
                    s.set_id_empresa(ef.get_id())
                    cls.atualizar(ef)
                    Setores.atualizar(s)
                else: raise Exception("Setor não pode ser movido de empresa nenhuma a empresa nenhuma.")
            else:
                if ef == None:
                    ei.set_setores(ei.get_setores()-1)
                    s.set_id_empresa(0)
                    cls.atualizar(ei)
                    Setores.atualizar(s)
                else:
                    if ei.get_id() != ef.get_id():
                        ei.set_setores(ei.get_setores()-1)
                        s.set_id_empresa(ef.get_id())
                        ef.set_setores(ef.get_setores()+1)
                        cls.atualizar(ei)
                        Setores.atualizar(s)
                        cls.atualizar(ef)
                    else: raise Exception("Não se pode mover o funcionário ao setor em que já está.")

    
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Projeto.2/data/empresas.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    e = Empresa(obj["id"], obj["nome"], obj["desc"], obj["dono"], dt.datetime.strptime(obj["fund"], "%d/%m/%Y").date(), obj["setores"], obj["custo_add"])
                    cls.objetos.append(e)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Projeto.2/data/empresas.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Empresa.to_json)



class Setores(CRUD):
    @classmethod
    def mover_func(cls, id_setor: int, id_func: int):
        sf = cls.listar_id(id_setor)
        f = Funcionarios.listar_id(id_func)
        if f != None:
            if f.get_nome() != "admin":
                si = cls.listar_id(f.get_id_setor())
                if si == None:
                    if sf != None:
                        sf.set_funcionarios(sf.get_funcionarios()+1)
                        f.set_id_setor(sf.get_id())
                        cls.atualizar(sf)
                        Funcionarios.atualizar(f)
                    else: raise Exception("Funcionário não pode ser movido de setor nenhum a setor nenhum.")
                else:
                    if sf == None:
                        si.set_funcionarios(si.get_funcionarios()-1)
                        f.set_id_setor(0)
                        cls.atualizar(si)
                        Funcionarios.atualizar(f)
                    else:
                        if si.get_id() != sf.get_id():
                            si.set_funcionarios(si.get_funcionarios()-1)
                            f.set_id_setor(sf.get_id())
                            sf.set_funcionarios(sf.get_funcionarios()+1)
                            cls.atualizar(si)
                            Funcionarios.atualizar(f)
                            cls.atualizar(sf)
                        else: raise Exception("Não se pode mover o funcionário ao setor em que já está.")
            else: raise Exception("Não se pode mover o admin.")   


    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Projeto.2/data/setores.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    n = Setor(obj["id"], obj["nome"], obj["desc"], dt.datetime.strptime(obj["data"], "%d/%m/%Y").date(), obj["funcionarios"], obj["id_empresa"], obj["custo_add"])
                    cls.objetos.append(n)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Projeto.2/data/setores.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Setor.to_json)




class Funcionarios(CRUD):
    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("Projeto.2/data/funcionarios.json", mode = "r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    f = Funcionario(obj["id"], obj["nome"], obj["senha"], obj["ocup"], obj["cpf"], obj["email"], obj["custo"], dt.datetime.strptime(obj["contr"], "%d/%m/%Y"), obj["id_setor"])
                    cls.objetos.append(f)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("Projeto.2/data/funcionarios.json", mode = "w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Funcionario.to_json)