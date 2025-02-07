import datetime as dt


class Funcionario:
    def __init__(self, id: int, nome: str, ocup: str, nasc: dt.date, cpf: int, email: str, custo: float, contr: dt.date, id_setor: int) -> None:
        self.id = id
        self.nome = nome
        self.ocup = ocup
        self.nasc = nasc
        self.cpf = cpf
        self.email = email
        self.custo = custo
        self.contr = contr
        self.id_setor = id_setor

    def __str__(self) -> str:
        return f"{self.id} - {self.nome} - {self.ocup}; Nascimento - {dt.date.strftime(self.nasc, '%d/%m/%Y')}; CPF - {self.cpf}; E-mail - {self.email}; Custo mensal - {self.custo}; Data de contratação: {dt.date.strftime(self.contr, '%d/%m/%Y')}; ID do setor: {self.id_setor}; ID da empresa: {self.id_empresa()}"

    def to_json(self):
        dic = {}
        dic["id"] = self.id
        dic["nome"] = self.nome
        dic["ocup"] = self.ocup
        dic["nasc"] = dt.date.strftime(self.nasc, "%d/%m/%Y")
        dic["cpf"] = self.cpf
        dic["email"] = self.email
        dic["custo"] = self.custo
        dic["contr"] = dt.date.strftime(self.contr, "%d/%m/%Y")
        dic["id_setor"] = self.id_setor
        return dic

    def set_id(self, id):
        self.__id = id
    def get_id(self):
        return self.__id

    def set_nome(self, nome):
        self.__nome = nome
    def get_nome(self):
        return self.__nome

    def set_ocup(self, ocup):
        self.__ocup = ocup
    def get_ocup(self):
        return self.__ocup

    def set_nasc(self, nasc):
        self.__nasc = nasc
    def get_nasc(self):
        return self.__nasc

    def set_cpf(self, cpf):
        self.__cpf = cpf
    def get_cpf(self):
        return self.__cpf

    def set_email(self, email):
        self.__email = email
    def get_email(self):
        return self.__email

    def set_custo(self, custo):
        self.__custo = custo
    def get_custo(self):
        return self.__custo

    def set_contr(self, contr):
        self.__contr = contr
    def get_contr(self):
        return self.__contr

    def set_id_setor(self, id_setor):
        self.__id_setor = id_setor
    def get_id_setor(self):
        return self.__id_setor