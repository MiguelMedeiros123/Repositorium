import json

class Servico:
  def __init__(self, id, d, v, t):
    self.id = id
    self.descricao = d
    self.valor = v
    self.duracao = t
  def __str__(self):
    return f"{self.id} - {self.descricao} - {self.valor} - {self.duracao}"

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
    if n != None:
      n.descricao = obj.descricao
      n.valor = obj.valor
      n.duracao = obj.duracao
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
      with open("servicos.json", mode = "r") as arquivo:
        texto = json.load(arquivo)
        for obj in texto:
          n = Servico(obj["id"], obj["nome"], obj["email"], obj["fone"])                     # dicionário
          cls.objetos.append(n)
    except FileNotFoundError:
      pass
  @classmethod
  def salvar(cls):
    with open("servicos.json", mode = "w") as arquivo:
      json.dump(cls.objetos, arquivo, default=vars)