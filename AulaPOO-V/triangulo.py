class Triangulo:
    def __init__(self):
        self.__b = 0
        self.__h = 0
    def set_base(self, valor):
        if valor >= 0: self.__b = valor
        else: raise ValueError('O valor da base não pode ser negativo.')
    def get_base(self):
        return self.__b
    def set_altura(self, valor):
        if valor >= 0: self.__h = valor
        else: raise ValueError('O valor da altura não pode ser negativo.')
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.__b * self.__h / 2