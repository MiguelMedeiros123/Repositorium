from models.crud import Empresas, Setores, Funcionarios, Empresa, Setor, Funcionario
import datetime as dt



def in_admin():
    i = False
    for f in funcionario_listar():
        if f.get_nome() == "admin": i = True
    if not i:
        funcionario_inserir("admin", "1234", "admin", "1234", "admin", 0, dt.date.today())

def autenticar(email: str, senha: str) -> dict:
    for f in funcionario_listar():
        if f.get_email() == email and f.get_senha() == senha:
            return {"id": f.get_id(), "nome": f.get_nome()}
    return None



def funcionario_inserir(nome: str, senha: str, ocup: str, cpf: str, email: str, custo: float, contr: dt.date):
    f = Funcionario(0, nome, senha, ocup, cpf, email, custo, contr, 0)
    Funcionarios.inserir(f)

def funcionario_listar():
    return Funcionarios.listar()

def funcionario_listar_id(id: int) -> Funcionario:
    return Funcionarios.listar_id(id)

def funcionario_atualizar(id: int, nome: str, senha: str, ocup: str, cpf: str, email: str, custo: float, contr: dt.date):
    fv = funcionario_listar_id(id)
    fn = Funcionario(id, nome, senha, ocup, cpf, email, custo, contr, fv.get_id_setor())
    Funcionarios.atualizar(fn)

def funcionario_excluir(id: int):
    f = Funcionario(id, "", "", "", "", "", "", "", "")
    Funcionarios.excluir(f)

def funcionario_listar_empresa(id_func: int) -> int:
    s = setor_listar_id(funcionario_listar_id(id_func).get_id_setor())
    if s == None: return 0
    else: return s.get_id_empresa()

def funcionario_busca(nome: str, ocup: str):
    n = list(nome)
    o = list(ocup)
    fun = funcionario_listar()
    if nome != "":
        ft = fun.copy()
        for f in fun:
            nf = list(f.get_nome())
            for i in range(0, len(n)):
                if n[i] != nf[i]:
                    ft.remove(f)
                    break
        fun = ft
    if ocup != "":
        ft = fun.copy()
        for f in fun:
            of = list(f.get_ocup())
            for i in range(0, len(o)):
                if o[i] != of[i]:
                    ft.remove(f)
                    break
        fun = ft
    return fun            



def funcionario_mover_setor(id_setor: int, id_func: int):
    Setores.mover_func(id_setor, id_func)

def multi_funcionario_mover_setor(ocup: str, id_setor_inicial: int, id_setor_final: int):
    fun = funcionario_listar()
    if ocup != "":
        fun = funcionario_busca("", ocup)
    ft = fun.copy()
    for f in fun:
        if f.get_id_setor() != id_setor_inicial: ft.remove(f)
    for f in ft:
        funcionario_mover_setor(id_setor_final, f.get_id())



def setor_inserir(nome: str, desc: str, data: dt.date, custo_add: float):
    s = Setor(0, nome, desc, data, 0, 0, custo_add)
    Setores.inserir(s)

def setor_listar():
    return Setores.listar()

def setor_listar_id(id: int) -> Setor:
    return Setores.listar_id(id)

def setor_atualizar(id: int, nome: str, desc: str, data: dt.date, custo_add: float):
    sv = setor_listar_id(id)
    sn = Setor(id, nome, desc, data, sv.get_funcionarios(), sv.get_id_empresa(), custo_add)
    Setores.atualizar(sn)

def setor_excluir(id: int):
    s = Setor(id, "", "", "", "", "", "")
    Setores.excluir(s)

def setor_funcionarios(id_setor: int):
    func = []
    for f in funcionario_listar():
        if f.get_id_setor() == id_setor: func.append()
    return func

def setor_custo(id: int) -> float:
    c = setor_listar_id(id).get_custo_add()
    for f in funcionario_listar():
        if f.get_id_setor() == id:
            c += f.get_custo()
    return c

def setor_reajuste_salarial(id_setor: int, percentual: float):
    for f in funcionario_listar():
        if f.get_id_setor() == id_setor:
            nc = f.get_custo()*percentual/100
            funcionario_atualizar(f.get_id(), f.get_nome(), f.get_senha(), f.get_ocup(), f.get_cpf(), f.get_email(), nc, f.get_contr())



def setor_mover_empresa(id_empresa: int, id_setor: int):
    Empresas.mover_setor(id_empresa, id_setor)

def multi_setor_mover_empresa(id_empresa_inicial: int, id_empresa_final: int):
    for s in setor_listar():
        if s.get_id_empresa() == id_empresa_inicial:
            setor_mover_empresa(id_empresa_final, s.get_id())



def empresa_inserir(nome: str, desc: str, dono: str, fund: dt.date, custo_add: float):
    e = Empresa(0, nome, desc, dono, fund, 0, custo_add)
    Empresas.inserir(e)

def empresa_listar():
    return Empresas.listar()

def empresa_listar_id(id: int) -> Empresa:
    return Empresas.listar_id(id)

def empresa_atualizar(id: int, nome: str, desc: str, dono: str, fund: dt.date, custo_add: float):
    ev = empresa_listar_id(id)
    en = Empresa(id, nome, desc, dono, fund, ev.get_setores(), custo_add)
    Empresas.atualizar(en)

def empresa_excluir(id: int):
    e = Empresa(id, "", "", "", "", "", "")
    Empresas.excluir(e)

def empresa_setores(id_empresa: int):
    setores = []
    for s in setor_listar():
        if s.get_id_empresa() == id_empresa: setores.append(s)
    return setores

def empresa_reajuste_gastos(id_empresa: int, percentual: float):
    for s in setor_listar():
        if s.get_id_empresa() == id_empresa:
            ngasto = s.get_custo_add()*percentual/100
            setor_atualizar(s.get_id(), s.get_nome(), s.get_desc(), s.get_data(), ngasto)

def empresa_reajuste_salarial(id_empresa: int, percentual: float):
    for s in setor_listar():
        if s.get_id_empresa() == id_empresa:
            setor_reajuste_salarial(s.get_id(), percentual)
                    

def empresa_custo(id: int) -> float:
    c = empresa_listar_id(id).get_custo_add()
    for s in setor_listar():
        if s.get_id_empresa() == id:
            c += setor_custo(s.get_id())
    return c