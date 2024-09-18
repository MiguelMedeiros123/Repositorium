from models import Funcionario, Funcionarios
import datetime as dt


def Funcionario_inserir(nome: str, ocup: str, nasc: dt.date, cpf: int, email: str, custo: str, contr: dt.date, id_setor: int):
    c = Funcionario(0, nome, ocup, nasc, cpf, email, custo, contr, id_setor)
    Funcionarios.inserir(c)

def funcionario_listar():
    return Funcionarios.listar()

def funcionario_atualizar(id: int, nome: str, ocup: str, nasc: dt.date, cpf: int, email: str, custo: str, contr: dt.date, id_setor: int):
    c = Funcionario(id, nome, ocup, nasc, cpf, email, custo, contr, id_setor)
    Funcionarios.atualizar(c)

def funcionario_excluir(id):
    Funcionarios.excluir(id)