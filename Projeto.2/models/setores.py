import datetime as dt


class Setor:
    def __init__(self, id: int, nome: str, desc: str, data: dt.date, funcionarios: int, id_empresa: int) -> None:
        self.set_id(id)
        self.set_nome(nome)
        self.set_desc(desc)
        self.set_data(data)
        self.set_funcionarios(funcionarios)
        self.set_id_empresa(id_empresa)

    def __str__(self) -> str:
        return f"{self.get_id()} - {self.get_nome()}; {self.get_desc()}; Criado a {dt.date.strftime(self.get_data(), '%d/%m/%Y')}; N.º de funcionários - {self.get_funcionarios()}; ID da empresa - {self.get_id_empresa()}"

    def to_json(self):
        dic = {}
        dic["id"] = self.get_id()
        dic["nome"] = self.get_nome()
        dic["desc"] = self.get_desc()
        dic["data"] = dt.date.strftime(self.get_data(), "%d/%m/%Y")
        dic["funcionarios"] = self.get_funcionarios()
        dic["id_empresa"] = self.get_id_empresa()
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

    def set_data(self, data):
        self.__data = data
    def get_data(self):
        return self.__data

    def set_funcionarios(self, funcionarios):
        self.__funcionarios = funcionarios
    def get_funcionarios(self):
        return self.__funcionarios

    def set_id_empresa(self, id_empresa):
        self.__id_empresa = id_empresa
    def get_id_empresa(self):
        return self.__id_empresa