# CRUD de clientes - cadastro de clientes - lista
# C - Create - insere um cliente no cadastro
# R - Read - lê os clientes cadastrados
# U - Update - atualiza os dados de um cliente
# D - Delete - remove um cliente do cadastro
import json
import datetime as dt
from servico import Servico, Servicos
from cliente import Cliente, Clientes
from horario import Horario, Horarios

class UI:
  @staticmethod
  def menu():
    print("1 - inserir cliente, 2 - listar clientes, 3 - atualizar cliente, 4 - excluir cliente")
    print("5 - inserir horário, 6 - listar horários, 7 - atualizar horário, 8 - excluir horário")
    print("9 - inserir serviço, 10 - listar serviços, 11 - atualizar serviço, 12 - excluir serviço")
    print("13 - fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 13: 
      op = UI.menu()
      if op == 1: UI.cliente_inserir()
      if op == 2: UI.cliente_listar()
      if op == 3: UI.cliente_atualizar()
      if op == 4: UI.cliente_excluir()
      if op == 5: UI.horario_inserir()
      if op == 6: UI.horario_listar()
      if op == 7: UI.horario_atualizar()
      if op == 8: UI.horario_excluir()
      if op == 9: UI.servico_inserir()
      if op == 10: UI.servico_listar()
      if op == 11: UI.servico_atualizar()
      if op == 12: UI.servico_excluir()

  @staticmethod
  def cliente_inserir():
    #id = int(input("Informe o id: "))
    nome = input("Informe o nome: ")
    email = input("Informe o e-mail: ")
    fone = input("Informe o fone: ")
    c = Cliente(0, nome, email, fone)
    Clientes.inserir(c)

  @staticmethod
  def cliente_listar():
    for c in Clientes.listar():
      print(c)

  @staticmethod
  def cliente_atualizar():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser atualizado: "))
    nome = input("Informe o novo nome: ")
    email = input("Informe o novo e-mail: ")
    fone = input("Informe o novo fone: ")
    c = Cliente(id, nome, email, fone)
    Clientes.atualizar(c)

  @staticmethod
  def cliente_excluir():
    UI.cliente_listar()
    id = int(input("Informe o id do cliente a ser excluído: "))
    c = Cliente(id, "", "", "")
    Clientes.excluir(c)

  @staticmethod
  def horario_inserir():
    dstr = dt.input("Insere uma data, no formato (dd/mm/aaaa hh:mm): ")
    d = dt.datetime.strptime(dstr, "%d/%M/%Y %h:%m")
    h = Horario(0, d)
    Horarios.inserir(h)
  
  @staticmethod
  def horario_listar():
    for n in Horarios.listar():
      print(n)

  @staticmethod
  def horario_atualizar():
    UI.horario_listar()
    id = int(input("Informe o id do horário a atualizar: "))
    d = dt.datetime.strptime(input("Insere o novo horário, no formato (dd/mm/aaaa hh:mm): "), "%d/%M/%Y %h:%m")
    n = Horario(id, d)
    Horarios.atualizar(n)

  @staticmethod
  def horario_excluir():
    UI.horario_listar()
    id = int(input("Insere o id do horário a ser excluído: "))
    n = Horario(id, "")
    Horarios.excluir(n)

  @staticmethod
  def servico_inserir():
    d = input("Insere uma descrição ao serviço: ")
    v = int(input("Insere um valor ao serviço: "))
    t = int(input("Insere uma duração ao serviço: "))
    n = Servico(0, d, v, t)
    Servicos.inserir(n)

  @staticmethod
  def servico_listar():
    for n in Horarios.listar():
      print(n)

  @staticmethod
  def servico_atualizar():
    UI.servico_listar()
    id = int(input("Informe o id do serviço a atualizar: "))
    d = input("Insere a nova descrição: ")
    v = int(input("Insere o novo valor: "))
    t = int(input("Insere a nova duração: "))
    n = Servico(id, d, v, t)
    Servicos.atualizar(n)
UI.main()