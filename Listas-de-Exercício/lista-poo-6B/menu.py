# CRUD de clientes - cadastro de clientes - lista
# C - Create - insere um cliente no cadastro
# R - Read - lê os clientes cadastrados
# U - Update - atualiza os dados de um cliente
# D - Delete - remove um cliente do cadastro
import json
import datetime as dt

# Modelo
class Cliente:
  def __init__(self, id, nome, email, fone):
    self.id = id
    self.nome = nome
    self.email = email
    self.fone = fone
  def __str__(self):
    return f"{self.id} - {self.nome} - {self.email} - {self.fone}"

class Horario:
  def __init__(self, id, d):
    self.id = id
    self.data = d
    self.confirmado = False
    self.idCliente = 0
    self.idServico = 0
  def __str__(self):
    return f"{self.id} - {self.data} - {self.confirmado} - {self.idCliente} - {self.idServico}"

class Servico:
  def __init__(self, id, d, v, t):
    self.id = id
    self.descricao = d
    self.valor = v
    self.duracao = t
  def __str__(self):
    return f"{self.id} - {self.descricao} - {self.valor} - {self.duracao}"
    

# Persistência
class Clientes:
  objetos = []  # atributo estático
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0                     # cálculo do maior id utilizado - começa com 0
    for c in cls.objetos:     # percorre a lista de clientes - c é cada cliente
      if c.id > m: m = c.id   # compara o id de c com m (maior)
    obj.id = m + 1  
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for c in cls.objetos:
      if c.id == id: return c
    return None 
  @classmethod
  def atualizar(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None:
       c.nome = obj.nome
       c.email = obj.email
       c.fone = obj.fone
    cls.salvar()   
  @classmethod
  def excluir(cls, obj):
    c = cls.listar_id(obj.id)
    if c != None: 
      cls.objetos.remove(c)
      cls.salvar()   
  @classmethod
  def salvar(cls):  
    with open("clientes.json", mode = "w") as arquivo:   # write
      json.dump(cls.objetos, arquivo, default = vars) 
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try: 
      with open("clientes.json", mode = "r") as arquivo:   # read
        texto = json.load(arquivo)
        for obj in texto:
          c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"])                     # dicionário
          cls.objetos.append(c)
    except FileNotFoundError:
      pass

class Horarios:
  objetos = []
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for n in cls.objetos:
      if n.id > m: m = n.id
    obj.id = m + 1
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for n in cls.objetos:
      if id == n.id: return n
    return None
  @classmethod
  def atualizar(cls, obj):
    n = cls.listar_id(obj.id)
    if n != None:
      n.data = obj.data
      n.confirmado = obj.confirmado
      n.idCliente = obj.idCliente
      n.idServico = obj.idServico
    cls.salvar()
  @classmethod
  def excluir(cls, obj):
    n = cls.listar_id(obj.id)
    if n != None:
      cls.objetos.remove(n)
      cls.salvar()
  @classmethod
  def abrir(cls):
    cls.objetos = []
    try:
      with open("horarios.json", mode = "r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:
          n = Horario(obj["id"], obj["data"])
          cls.objetos.append(n)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("horarios.json", mode = "w") as arquivo:
      json.dump(cls.objetos, arquivo, default = vars)

class Servicos:
  objetos = []
  @classmethod
  def inserir(cls, obj):
    cls.abrir()
    m = 0
    for n in cls.objetos:
      if n.id > m: m = n.id
    obj.id = m + 1
    cls.objetos.append(obj)
    cls.salvar()
  @classmethod
  def listar(cls):
    cls.abrir()
    return cls.objetos
  @classmethod
  def listar_id(cls, id):
    cls.abrir()
    for n in cls.objetos:
      if n.id == id: return n
    return None
  @classmethod
  def atualizar(cls, obj):
    n = cls.listar_id(obj.id)

# Visão
class UI:
  @staticmethod
  def menu():
    print("1 - Inserir cliente, 2 - listar clientes, 3 - atualizar cliente, 4 - excluir cliente, 9 - fim")
    return int(input("Informe uma opção: "))

  @staticmethod
  def main():
    op = 0
    while op != 9: 
      op = UI.menu()
      if op == 1: UI.cliente_inserir()
      if op == 2: UI.cliente_listar()
      if op == 3: UI.cliente_atualizar()
      if op == 4: UI.cliente_excluir()

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

UI.main()