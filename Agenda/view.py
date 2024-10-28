from models import Cliente, Clientes, Horario, Horarios, Servico, Servicos



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



# def horario_inserir(1xxxxxx):
#     h = Horario(0, xxxxx)
#     Horarios.inserir(h)

# def horario_listar() -> list:
#     return Horarios.listar()

# def horario_atualizar(1xxxxxxx):
#     h = Horario(xxxxxxx)
#     Horarios.atualizar(h)

# def horario_excluir(id: int):
#     h = Horario(id, xxxxxx)
#     Horarios.excluir(h)



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