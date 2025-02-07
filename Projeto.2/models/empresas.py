import datetime as dt


class Empresa:
    def __init__(self, id: int, nome: str, desc: str, dono: str, fund: dt.date, setores: int):
        self.set_id(id)
        self.set_nome(nome)
        self.set_desc(desc)
        self.set_dono(dono)
        self.set_fund(fund)
        self.set_setores(setores)
        
    def __str__(self) -> str:
        return f"{self.id} - {self.nome}; {self.desc}; Dono - {self.dono}; Fundada a {dt.date.strftime(self.fund, '%d/%m/%Y')}; N.º de setores: {self.setores}; Gasto mensal: {self.custo()}"

    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["desc"] = self.desc
        dic["dono"] = self.dono
        dic["fund"] = dt.date.strftime(self.fund, "%d/%m/%Y")
        dic["setores"] = self.setores
        return dic

    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome

    def set_desc(self, desc):
        self.__desc = desc
    def get_desc(self):
        return self.__desc

    def set_dono(self, dono):
        self.__dono = dono
    def get_dono(self):
        return self.__dono

    def set_fund(self, fund):
        self.__fund = fund
    def get_fund(self):
        return self.__fund

    def set_setores(self, setores):
        self.__setores = setores
    def get_setores(self):
        return self.__setores