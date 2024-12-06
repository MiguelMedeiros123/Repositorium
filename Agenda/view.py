from models.clientes import *
from models.horarios import *
from models.servicos import *



def cliente_admin():
    for c in cliente_listar():
        if c.get_nome() == "admin": return
    cliente_inserir("admin", "admin", "1234", "1234")

def cliente_inserir(nome: str, email: str, fone: str, senha: str):
    for cli in cliente_listar():
        if email == cli.get_email(): raise ValueError("E-mail informado já está em uso.")
    c = Cliente(0, nome, email, fone, senha)
    Clientes.inserir(c)

def cliente_listar() -> list:
    return Clientes.listar()

def cliente_listar_id(id: int) -> Cliente:
    for c in cliente_listar():
        if c.get_id() == id: return c
    return None

def cliente_atualizar(id: int, nome: str, email: str, fone: str, senha: str):
    for cli in cliente_listar():
        if id != cli.get_id() and email == cli.get_email(): raise ValueError("E-mail informado já está em uso.")
    c = Cliente(id, nome, email, fone, senha)
    Clientes.atualizar(c)

def cliente_excluir(id: int):
    for h in horario_listar():
        if h.get_idCliente() == id: raise ValueError("Cliente informado possui horário marcado.")
    c = Cliente(id, "-", "-", "-", "-")
    Clientes.excluir(c)

def cliente_autenticar(email: str, senha: str) -> dict:
    for c in cliente_listar():
        if c.get_email() == email and c.get_senha() == senha:
            return {"id": c.get_id(), "nome": c.get_nome()}
    return None



def horario_inserir(data: dt.datetime, confirmado: bool, idCliente: int, idServico: int):
    isc = False
    for c in cliente_listar():
        if c.get_id() == idCliente: isc = True
    if not isc and idCliente != 0: raise ValueError("ID do cliente informado não existe.")
    iss = False
    for s in servico_listar():
        if s.get_id() == idServico: iss = True
    if not iss and idServico != 0: raise ValueError("ID do serviço informado não existe.")
    h = Horario(0, data, confirmado, idCliente, idServico)
    Horarios.inserir(h)

def horario_listar() -> list:
    return Horarios.listar()

def horario_listar_id(id: int) -> Horario:
    for h in horario_listar():
        if h.get_id() == id: return h
    return None

def horario_atualizar(id: int, data: dt.datetime, confirmado: bool, idCliente: int, idServico: int):
    isc = False
    for c in cliente_listar():
        if c.get_id() == idCliente: isc = True
    if not isc and idCliente != 0: raise ValueError("ID do cliente informado não existe.")
    iss = False
    for s in servico_listar():
        if s.get_id() == idServico: iss = True
    if not iss and idServico != 0: raise ValueError("ID do serviço informado não existe.")
    h = Horario(id, data, confirmado, idCliente, idServico)
    Horarios.atualizar(h)

def horario_excluir(id: int):
    for c in cliente_listar():
        if c.get_id() == horario_listar_id(id).get_idCliente(): raise ValueError("Horário informado está marcado para um cliente.")
    h = Horario(id, "-", "-", "-", "-")
    Horarios.excluir(h)

def horario_abrir_agenda(data: str, hora_inicio: str, hora_fim: str, intervalo: int):
    hora = dt.datetime.strptime(f"{data} {hora_inicio}", "%d/%m/%Y %H:%M")
    if hora < dt.datetime.now(): raise ValueError("Dia/horário inicial informado já passou.")
    horamax = dt.datetime.strptime(f"{data} {hora_fim}", "%d/%m/%Y %H:%M")
    if horamax < hora: raise ValueError("Horário final é anterior ao horário de início.")
    delta = dt.timedelta(minutes=intervalo)
    if delta.total_seconds() <= 0: raise ValueError("Intervalo entre horários é inválido") 
    
    while hora < horamax:
        horario_inserir(hora, False, 0, 0)
        hora += delta
    horario_inserir(horamax, False, 0, 0)

def horario_disponivel_listar():
    horarios = []
    for h in horario_listar():
        if h.get_data() >= dt.datetime.now() and h.get_idCliente() == 0: horarios.append(h)
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
    for h in horario_listar():
        if h.get_idServico() == id: raise ValueError("Serviço informado é prestado em horário(s).")
    s = Servico(id, "-", 0, 0)
    Servicos.excluir(s)