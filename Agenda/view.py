from models.clientes import *
from models.horarios import *
from models.servicos import *
from models.perfis import *
from models.profissionais import *


def autenticar(email: str, senha: str) -> dict:
    for c in cliente_listar():
        if c.get_email() == email and c.get_senha() == senha:
            return {"id": c.get_id(), "nome": c.get_nome(), "tipo": "cliente"}
    for p in profissional_listar():
        if p.get_email() == email and p.get_senha() == senha:
            return {"id": p.get_id(), "nome": p.get_nome(), "tipo": "profissional"}
    return None

def cliente_admin():
    for c in cliente_listar():
        if c.get_nome() == "admin": return
    cliente_inserir("admin", "admin", "1234", "1234", 0)


def cliente_inserir(nome: str, email: str, fone: str, senha: str, idPerfil: int):
    for cli in cliente_listar():
        if email == cli.get_email(): raise ValueError("E-mail informado já está em uso.")
    for pro in profissional_listar():
        if email == pro.get_email(): raise ValueError("E-mail informado já está em uso.")
    c = Cliente(0, nome, email, fone, senha, idPerfil)
    Clientes.inserir(c)

def cliente_listar() -> list:
    return Clientes.listar()

def cliente_listar_id(id: int) -> Cliente:
    Clientes.listar_id(id)

def cliente_atualizar(id: int, nome: str, email: str, fone: str, senha: str, idPerfil: int):
    for cli in cliente_listar():
        if id != cli.get_id() and email == cli.get_email(): raise ValueError("E-mail informado já está em uso.")
    for pro in profissional_listar():
        if email == pro.get_email(): raise ValueError("E-mail informado já está em uso.")
    c = Cliente(id, nome, email, fone, senha, idPerfil)
    Clientes.atualizar(c)

def cliente_excluir(id: int):
    for h in horario_listar():
        if h.get_idCliente() == id: raise ValueError("Cliente informado possui horário marcado.")
    c = Cliente(id, "-", "-", "-", "-", 0)
    Clientes.excluir(c)



def horario_inserir(data: dt.datetime, confirmado: bool, idCliente: int, idServico: int, idProfissional: int):
    isc = False
    for c in cliente_listar():
        if c.get_id() == idCliente: isc = True
    if not isc and idCliente != 0: raise ValueError("ID do cliente informado não existe.")
    iss = False
    for s in servico_listar():
        if s.get_id() == idServico: iss = True
    if not iss and idServico != 0: raise ValueError("ID do serviço informado não existe.")
    isp = False
    for p in profissional_listar():
        if p.get_id() == idProfissional: isp = True
    if not isp and idProfissional != 0: raise ValueError("ID do serviço informado não existe.")
    h = Horario(0, data, confirmado, idCliente, idServico, idProfissional)
    Horarios.inserir(h)

def horario_listar() -> list:
    return Horarios.listar()

def horario_listar_id(id: int) -> Horario:
    Horarios.listar_id(id)

def horario_atualizar(id: int, data: dt.datetime, confirmado: bool, idCliente: int, idServico: int, idProfissional: int):
    isc = False
    for c in cliente_listar():
        if c.get_id() == idCliente: isc = True
    if not isc and idCliente != 0: raise ValueError("ID do cliente informado não existe.")
    iss = False
    for s in servico_listar():
        if s.get_id() == idServico: iss = True
    if not iss and idServico != 0: raise ValueError("ID do serviço informado não existe.")
    isp = False
    for p in profissional_listar():
        if p.get_id() == idProfissional: isp = True
    if not isp and idProfissional != 0: raise ValueError("ID do serviço informado não existe.")
    h = Horario(id, data, confirmado, idCliente, idServico, idProfissional)
    Horarios.atualizar(h)

def horario_excluir(id: int):
    for c in cliente_listar():
        if c.get_id() == horario_listar_id(id).get_idCliente(): raise ValueError("Horário informado está marcado para um cliente.")
    h = Horario(id, "-", "-", "-", "-", "-")
    Horarios.excluir(h)

def horario_abrir_agenda(data: str, hora_inicio: str, hora_fim: str, intervalo: int):
    hora = dt.datetime.strptime(f"{data} {hora_inicio}", "%d/%m/%Y %H:%M")
    if hora < dt.datetime.now(): raise ValueError("Dia/horário inicial informado já passou.")
    horamax = dt.datetime.strptime(f"{data} {hora_fim}", "%d/%m/%Y %H:%M")
    if horamax < hora: raise ValueError("Horário final é anterior ao horário de início.")
    delta = dt.timedelta(minutes=intervalo)
    if delta.total_seconds() <= 0: raise ValueError("Intervalo entre horários é inválido") 
    
    while hora < horamax:
        horario_inserir(hora, False, 0, 0, 0)
        hora += delta
    horario_inserir(horamax, False, 0, 0, 0)

def horario_disponivel_listar():
    horarios = []
    for h in horario_listar():
        if h.get_data() >= dt.datetime.now() and h.get_idCliente() == 0: horarios.append(h)
    return horarios

def horario_profissional_listar(id: int):
    horarios = []
    for h in horario_listar():
        if h.get_idProfissional() == id: horarios.append(h)
    return horarios




def servico_inserir(descricao: str, valor: float, duracao: int):
    s = Servico(0, descricao, valor, duracao)
    Servicos.inserir(s)

def servico_listar() -> list:
    return Servicos.listar()

def servico_listar_id(id: int) -> Servico:
    Servicos.listar_id(id)

def servico_atualizar(id: int, descricao: str, valor: float, duracao: int):
    s = Servico(id, descricao, valor, duracao)
    Servicos.atualizar(s)

def servico_excluir(id: int):
    for h in horario_listar():
        if h.get_idServico() == id: raise ValueError("Serviço informado é prestado em horário(s).")
    s = Servico(id, "-", 0, 0)
    Servicos.excluir(s)



def profissional_inserir(nome: str, especialidade: str, conselho: str, email: str, senha: str):
    for cli in cliente_listar():
        if email == cli.get_email(): raise ValueError("E-mail informado já está em uso.")
    for pro in profissional_listar():
        if email == pro.get_email(): raise ValueError("E-mail informado já está em uso.")
    p = Profissional(0, nome, especialidade, conselho, email, senha)
    Profissionais.inserir(p)

def profissional_listar() -> list:
    return Profissionais.listar()

def profissional_listar_id(id: int) -> Profissional:
    Profissionais.listar_id(id)

def profissional_atualizar(id: int, nome: str, especialidade: str, conselho: str, email: str, senha: str):
    for cli in cliente_listar():
        if email == cli.get_email(): raise ValueError("E-mail informado já está em uso.")
    for pro in profissional_listar():
        if email == pro.get_email() and id != pro.get_id(): raise ValueError("E-mail informado já está em uso.")
    p = Profissional(id, nome, especialidade, conselho, email, senha)
    Profissionais.atualizar(p)

def profissional_excluir(id: int):
    for h in horario_listar():
        if h.get_idProfissional() == id: raise ValueError("Profissional informado possui horário marcado.")
    p = Profissional(id, "-", "-", "-", "-", "-")
    Profissionais.excluir(p)



def perfil_inserir(nome: str, descricao: str, beneficios: str):
    p = Perfil(0, nome, descricao, beneficios)
    Perfis.inserir(p)

def perfil_listar() -> list:
    return Perfis.listar()

def perfil_listar_id(id: int) -> Perfil:
    Perfis.listar_id(id)

def perfil_atualizar(id: int, nome: str, descricao: str, beneficios: str):
    p = Perfil(id, nome, descricao, beneficios)
    Perfis.atualizar(p)

def perfil_excluir(id: int):
    for c in cliente_listar():
        if c.get_idPerfil() == id: raise ValueError("Usuário(s) usa(m) o perfil indicado.")
    p = Perfil(id, "-", "-", "-")
    Perfis.excluir(p)