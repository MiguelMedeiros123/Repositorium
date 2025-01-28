from models.funcionarios import Funcionario, Funcionarios
from models.setores import Setor, Setores
from models.empresas import Empresa, Empresas
import datetime as dt


def funcionario_inserir(nome: str, ocup: str, nasc: dt.date, cpf: int, email: str, custo: float, contr: dt.date):
    f = Funcionario(0, nome, ocup, nasc, cpf, email, custo, contr, 0)
    Funcionarios.inserir(f)

def funcionario_listar():
    return Funcionarios.listar()

def funcionario_atualizar(id: int, nome: str, ocup: str, nasc: dt.date, cpf: int, email: str, custo: float, contr: dt.date):
    f = Funcionario(id, nome, ocup, nasc, cpf, email, custo, contr, 0)
    Funcionarios.atualizar(f)

def funcionario_excluir(id: int):
    Funcionarios.excluir(id)

def funcionario_mover_setor(id_func: int, id_setor: int):
    Funcionarios.mover_setor(id_func, id_setor)

def funcionario_listar_setor(id_setor: int):
    return Funcionarios.listar_setor(id_setor)

def setor_inserir(nome: str, desc: str, data: dt.date):
    s = Setor(0, nome, desc, data, 0, 0)
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

def setor_mover_empresa(id_setor: int, id_empresa: int):
    Setores.mover_empresa(id_setor, id_empresa)

def setor_listar_empresa(id_empresa: int):
    return Setores.listar_empresa(id_empresa)

def empresa_inserir(nome: str, desc: str, dono: str, fund: dt.date):
    e = Empresa(0, nome, desc, dono, fund, 0)
    Empresas.inserir(e)

def empresa_listar():
    return Empresas.listar()

def empresa_listar_id(id: int):
    return Empresas.listar_id(id)

def empresa_atualizar(id: int, nome: str, desc: str, dono: str, fund: dt.date):
    e = Empresa(id, nome, desc, dono, fund, 0)
    Empresas.atualizar(e)

def empresa_excluir(id: int):
    Empresas.excluir(id)