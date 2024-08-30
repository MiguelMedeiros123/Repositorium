import json
import datetime as dt

class Horario:
  def __init__(self, id, d):
    self.id = id
    self.data = d
    self.confirmado = False
    self.idCliente = 0
    self.idServico = 0
  def __str__(self):
    return f"{self.id} - {self.data} - {self.confirmado} - {self.idCliente} - {self.idServico}"
  
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