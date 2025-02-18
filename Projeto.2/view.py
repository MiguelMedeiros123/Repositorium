from models.crud import Empresas, Setores, Funcionarios, Empresa, Setor, Funcionario
import datetime as dt


def in_admin():
    i = False
    for f in funcionario_listar():
        if f.get_nome() == "admin": i = True
    if not i:
        funcionario_inserir("admin", "1234", "admin", "1234", "admin", 0, dt.date.today())

def autenticar(email: str, senha: str) -> dict:
    for f in funcionario_listar():
        if f.get_email() == email and f.get_senha() == senha:
            return {"id": f.get_id(), "nome": f.get_nome(), "tipo": "cliente"}
    return None


def funcionario_inserir(nome: str, senha: str, ocup: str, cpf: str, email: str, custo: float, contr: dt.date):
    f = Funcionario(0, nome, senha, ocup, cpf, email, custo, contr, 0)
    Funcionarios.inserir(f)

def funcionario_listar():
    return Funcionarios.listar()

def funcionario_listar_id(id: int) -> Funcionario:
    return Funcionarios.listar_id(id)

def funcionario_atualizar(id: int, nome: str, senha: str, ocup: str, cpf: str, email: str, custo: float, contr: dt.date):
    f = Funcionario(id, nome, senha, ocup, cpf, email, custo, contr, 0)
    Funcionarios.atualizar(f)

def funcionario_excluir(id: int):
    f = Funcionario(id, "", "", "", "", "", "", "", "")
    Funcionarios.excluir(f)

def funcionario_mover_setor(id_func: int, id_setor: int):
    Funcionarios.mover_setor(id_func, id_setor)

def funcionario_listar_empresa(id_func) -> int:
    f = funcionario_listar_id(id_func)
    s = setor_listar_id(f.get_id_setor())
    if s == None: return 0
    else: return s.get_id_empresa()

def setor_inserir(nome: str, desc: str, data: dt.date):
    s = Setor(0, nome, desc, data, 0, 0)
    Setores.inserir(s)

def setor_listar():
    return Setores.listar()

def setor_listar_id(id: int) -> Setor:
    return Setores.listar_id(id)

def setor_atualizar(id: int, nome: str, desc: str, data: dt.date):
    s = Setor(id, nome, desc, data, 0, 0)
    Setores.atualizar(s)

def setor_excluir(id: int):
    s = Setor(id, "", "", "", "", "")
    Setores.excluir(s)

def setor_mover_empresa(id_setor: int, id_empresa: int):
    Setores.mover_empresa(id_setor, id_empresa)

def setor_listar_empresa(id_empresa: int):
    return Setores.listar_empresa(id_empresa)

def setor_custo(id: int) -> float:
    c = 0
    for f in funcionario_listar():
        if f.get_id_setor() == id:
            c += f.get_custo()
    return c

def empresa_inserir(nome: str, desc: str, dono: str, fund: dt.date):
    e = Empresa(0, nome, desc, dono, fund, 0)
    Empresas.inserir(e)

def empresa_listar():
    return Empresas.listar()

def empresa_listar_id(id: int) -> Empresa:
    return Empresas.listar_id(id)

def empresa_atualizar(id: int, nome: str, desc: str, dono: str, fund: dt.date):
    e = Empresa(id, nome, desc, dono, fund, 0)
    Empresas.atualizar(e)

def empresa_excluir(id: int):
    e = Empresa(id, "", "", "", "", "")
    Empresas.excluir(e)

def empresa_custo(id: int) -> float:
    c = 0
    for s in setor_listar():
        if s.get_id_empresa() == id:
            c += setor_custo(s.get_id())
    return c