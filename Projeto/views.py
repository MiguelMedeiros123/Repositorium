from models import Funcionario, Funcionarios, Setor, Setores, Empresa, Empresas
import datetime as dt


def funcionario_inserir(nome: str, ocup: str, nasc: dt.date, cpf: int, email: str, custo: str, contr: dt.date):
    f = Funcionario(0, nome, ocup, nasc, cpf, email, custo, contr, 0)
    Funcionarios.inserir(f)

def funcionario_listar():
    return Funcionarios.listar()

def funcionario_listar_id(id: int):
    return Funcionarios.listar_id(id)

def funcionario_atualizar(id: int, nome: str, ocup: str, nasc: dt.date, cpf: int, email: str, custo: str, contr: dt.date, id_setor: int):
    f = Funcionario(id, nome, ocup, nasc, cpf, email, custo, contr, id_setor)
    Funcionarios.atualizar(f)

def funcionario_excluir(id: int):
    Funcionarios.excluir(id)

def setor_inserir(nome: str, desc: str, data: dt.date):
    s = Setor(0, nome, desc, data, [], 0)
    Setores.inserir(s)

def setor_listar():
    return Setores.listar()

def setor_listar_id(id: int):
    return Setores.listar_id(id)

def setor_atualizar(id: int, nome: str, desc: str, data: dt.date):
    s = Setor(id, nome, desc, data, 0, 0)
    Setores.atualizar(s)

def setor_excluir(id: int):
    Setores.excluir(id)

def setor_inserir_func(id_setor: int, id_func: int):
    Setores.inserir_func(id_setor, id_func)

def setor_listar_func(id_setor: int):
    return Setores.listar_func(id_setor)

def setor_listar_func_id(id_setor: int, id_func: int):
    return Setores.listar_func_id(id_setor, id_func)

def setor_remover_func(id_setor: int, id_func: int):
    Setores.remover_func(id_setor, id_func)

def empresa_inserir(nome: str, desc: str, dono: str):
    e = Empresa(0, nome, desc, dono)
    Empresas.inserir(e)

def empresa_listar():
    return Empresas.listar()

def empresa_atualizar(id: int, nome: str, desc: str, dono: str):
    e = Empresa(id, nome, desc, dono)
    Empresas.atualizar(e)

def empresa_excluir(id: int):
    Empresas.excluir(id)