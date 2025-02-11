import datetime as dt


class Funcionario:
    def __init__(self, id: int, nome: str, ocup: str, nasc: dt.date, cpf: int, email: str, custo: float, contr: dt.date, id_setor: int) -> None:
        self.set_id(id)
        self.set_nome(nome)
        self.set_ocup(ocup)
        self.set_nasc(nasc)
        self.set_cpf(cpf)
        self.set_email(email)
        self.set_custo(custo)
        self.set_contr(contr)
        self.set_id_setor(id_setor)

    def __str__(self) -> str:
        return f"{self.get_id()} - {self.get_nome()} - {self.get_ocup()}; Nascimento - {dt.date.strftime(self.get_nasc(), '%d/%m/%Y')}; CPF - {self.get_cpf()}; E-mail - {self.get_email()}; Custo mensal - {self.get_custo()}; Data de contratação: {dt.date.strftime(self.get_contr(), '%d/%m/%Y')}; ID do setor: {self.get_id_setor()}"

    def to_json(self):
        dic = {}
        dic["id"] = self.get_id()
        dic["nome"] = self.get_nome()
        dic["ocup"] = self.get_ocup()
        dic["nasc"] = dt.date.strftime(self.get_nasc(), "%d/%m/%Y")
        dic["cpf"] = self.get_cpf()
        dic["email"] = self.get_email()
        dic["custo"] = self.get_custo()
        dic["contr"] = dt.date.strftime(self.get_contr(), "%d/%m/%Y")
        dic["id_setor"] = self.get_id_setor()
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