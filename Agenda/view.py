from models.clientes import *
from models.horarios import *
from models.servicos import *



def cliente_admin():
    for c in cliente_listar():
        if c.nome == "admin": return
    cliente_inserir("admin", "admin", "1234", "1234")

def cliente_inserir(nome: str, email: str, fone: str, senha: str):
    c = Cliente(0, nome, email, fone, senha)
    Clientes.inserir(c)

def cliente_listar() -> list:
    return Clientes.listar()

def cliente_listar_id(id: int) -> Cliente:
    for c in cliente_listar():
        if c.id == id: return c
    return None

def cliente_atualizar(id: int, nome: str, email: str, fone: str, senha: str):
    c = Cliente(id, nome, email, fone, senha)
    Clientes.atualizar(c)

def cliente_excluir(id: int):
    c = Cliente(id, "", "", "", "")
    Clientes.excluir(c)

def cliente_autenticar(email: str, senha: str) -> dict:
    for c in cliente_listar():
        if c.email == email and c.senha == senha:
            return {"id": c.id, "nome": c.nome}
    return None



def horario_inserir(data: dt.datetime, confirmado: bool, idCliente: int, idServico: int):
    h = Horario(0, data, confirmado, idCliente, idServico)
    Horarios.inserir(h)

def horario_listar() -> list:
    return Horarios.listar()

def horario_listar_id(id: int) -> Horario:
    for h in horario_listar():
        if h.id == id: return h
    return None

def horario_atualizar(id: int, data: dt.datetime, confirmado: bool, idCliente: int, idServico: int):
    h = Horario(id, data, confirmado, idCliente, idServico)
    Horarios.atualizar(h)

def horario_excluir(id: int):
    h = Horario(id, "", "", "", "")
    Horarios.excluir(h)

def horario_abrir_agenda(data: str, hora_inicio: str, hora_fim: str, intervalo: int):
    hora = dt.datetime.strptime(f"{data} {hora_inicio}", "%d/%m/%Y %H:%M")
    delta = dt.timedelta(minutes=intervalo)
    horamax = dt.datetime.strptime(f"{data} {hora_fim}", "%d/%m/%Y %H:%M")
    while hora < horamax:
        horario_inserir(hora, False, 0, 0)
        hora += delta
    horario_inserir(horamax, False, 0, 0)

def horario_disponivel_listar():
    horarios = []
    for h in horario_listar():
        if h.data >= dt.datetime.now() and h.idCliente == 0: horarios.append(h)
    return horarios



def servico_inserir(descricao: str, valor: float, duracao: int):
    s = Servico(0, descricao, valor, duracao)
    Servicos.inserir(s)

def servico_listar() -> list:
    return Servicos.listar()

def servico_atualizar(id: int, descricao: str, valor: float, duracao: int):
    s = Servico(id, descricao, valor, duracao)
    Servicos.atualizar(s)

def servico_excluir(id: int):
    s = Servico(id, "", "", "")
    Servicos.excluir(s)