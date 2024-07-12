class Corrida:
    def __init__(self):
        self.__distancia = 1
        self.__horas = 0
        self.__minutos = 0
        self.__segundos = 0

    def set_distancia(self, distancia):
        if distancia > 0: self.__distancia = distancia # validação
        else: raise ValueError("Distância há de ser positiva.")
    def get_distancia(self):
        return self.__distancia # formato h:m:s
    def set_tempo(self, tempo):
        t = tempo.split(":")
        self.__horas = int(t[0])
        self.__minutos = int(t[1])
        self.__segundos = int(t[2])
        if self.__horas < 0 or self.__minutos < 0 or self.__segundos < 0 or self.__horas + self.__minutos + self.__segundos == 0:
            raise ValueError("O valor de tempo informado é inválido.")
    def get_tempo(self):
        return f"{self.__horas}:{self.__minutos}:{self.__segundos}"
    def pace(self):
        t = self.__horas * 60 + self.__minutos + self.__segundos / 60
        d = self.__distancia / 1000
        return t/d