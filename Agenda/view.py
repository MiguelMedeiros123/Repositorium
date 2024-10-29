from models import clientes, horarios, servicos
import datetime as dt


def cliente_inserir(nome: str, email: str, fone: str, senha: str):
    c = Cliente(0, nome, email, fone, senha)
    Clientes.inserir(c)

def cliente_listar() -> list:
    return Clientes.listar()

def cliente_atualizar(id: int, nome: str, email: str, fone: str, senha: str):
    c = Cliente(id, nome, email, fone, senha)
    Clientes.atualizar(c)

def cliente_excluir(id: int):
    c = Cliente(id, "", "", "", "")
    Clientes.excluir(c)



def horario_inserir(data: dt.datetime, confirmado: bool, idCliente: int, idServico: int):
    h = Horario(0, data, confirmado, idCliente, idServico)
    Horarios.inserir(h)

def horario_listar() -> list:
    return Horarios.listar()

def horario_atualizar(id: int, data: dt.datetime, confirmado: bool, idCliente: int, idServico: int):
    h = Horario(id, data, confirmado, idCliente, idServico)
    Horarios.atualizar(h)

def horario_excluir(id: int):
    h = Horario(id, "", "", "", "")
    Horarios.excluir(h)



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