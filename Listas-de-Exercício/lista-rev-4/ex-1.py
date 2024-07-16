class Agua:
    def __init__(self):
        self.__mes = 0
        self.__ano = 0
        self.__consumo = 0
    def set_mes(self, mes):
        if mes > 0 and mes <= 12: self.__mes = mes
        else: raise ValueError('Insere um mês válido.')
    def set_ano(self, ano):
        if ano > 0: self.__ano = ano
        else: raise ValueError('Insere um ano válido')
    def set_consumo(self, consumo):
        if consumo > 0: self.__consumo = consumo
        else: raise ValueError('Insere um valor de consumo válido, em metros cúbicos.')
    def get_mes(self):
        return self.__mes
    def get_ano(self):
        return self.__ano
    def get_consumo(self):
        return self.__consumo
    def calc_conta(self):
        v = 0
        if self.__consumo <= 10: v = 38
        elif self.__consumo <= 20:
            v = 38 + (self.__consumo - 10) * 5
        else:
            v = 58 + (self.__consumo - 20) * 6

        return print(f"A conta de água do mês {self.__mes}/{self.__ano} é de {v} reais.")


a = Agua()

mes = int(input('Informa teu mês: '))
a.set_mes(mes)

ano = int(input('Informa teu ano: '))
a.set_ano(ano)

consumo = int(input('Informa teu consumo: '))
a.set_consumo(consumo)

a.calc_conta()