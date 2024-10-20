from model import Cliente, Clientes


def cliente_inserir(nome: str, email: str, fone: str):
    c = Cliente(0, nome, email, fone)
    Clientes.inserir(c)

def cliente_listar() -> list:
    return Clientes.listar()

def cliente_atualizar(id: int, nome: str, email: str, fone: str):
    c = Cliente(id, nome, email, fone)
    Clientes.atualizar(c)

def cliente_excluir(id: int):
    c = Cliente(id, "", "", "")
    Clientes.excluir(c)