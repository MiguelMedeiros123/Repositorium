class Ingresso:
    def __init__(self) -> None:
        self.__dia = ''
        self.__hora = 0
        self.semana = ['DOMINGO', 'SEGUNDA-FEIRA', 'TERÇA-FEIRA', 'QUARTA-FEIRA', 'QUINTA-FEIRA', 'SEXTA-FEIRA', 'SÁBADO']

    def set_dia(self, dia):
        d = False
        for x in range(len(self.semana)):
            if d == True: break
            if dia.upper() == self.semana[x]: d = True
        if d == True: self.__dia = dia
        else: raise ValueError('Insere um dia válido.')

    def set_hora(self, h):
        if h >= 0 and h < 24: self.__hora = h
        else: raise ValueError('Insere uma hora válida.')

    def get_dia(self):
        return self.__dia
    
    def get_hora(self):
        return self.__hora
    
    def calc_ingresso(self):
        valor = 0
        if self.__dia.upper() == 'QUINTA-FEIRA':
            valor = 6
        else:
            if self.__hora <= 16:
                valor = 5
            else:
                valor = 10
    
        return print(f'O valor do ingresso para {self.__hora}, às {self.__hora}, será de {valor} reais.')