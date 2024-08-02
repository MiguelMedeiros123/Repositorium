class Jogador:
    def __init__(self, nome: str, camisa: int, gols: int):
        if nome != "": self.SetNome(nome)
        if camisa >= 0: self.SetCamisa(camisa)
        if gols >= 0: self.SetGols(gols)
    def SetNome(self, nome: str):
        self.__nome = nome
    def SetCamisa(self, camisa: str):
        self.__camisa = camisa
    def SetGols(self, gols: int):
        self.__gols = gols
    def GetNome(self):
        return self.__nome
    def GetCamisa(self):
        return self.__camisa
    def GetGols(self):
        return self.__gols
    def __str__(self):
        return f"Nome: {self.GetNome()}; Camisa: {self.GetCamisa()}; Gols: {self.GetGols()}"
    
class Time:
    def __init__(self, nome: str, estado: str):
        if nome != "": self.__nome = nome
        if estado != "": self.__estado = estado
        self.__jogadores = []
    def Inserir(self, j: Jogador):
        self.__jogadores.append(j)
    def Listar(self):
        return self.__jogadores
    def Artilheiro(self):
        a = self.__jogadores[0]
        for x in self.__jogadores:
            if x.GetGols() > a.GetGols(): a = x
        return a
    def __str__(self):
        return f"Nome: {self.__nome}; Estado: {self.__estado}; Jogadores: {self.Listar()}"


jog1 = Jogador('pepe', 7, 10)
jog2 = Jogador('ding', 10, 20)
jog3 = Jogador('bubu', 9, 15)

team = Time('team', 'RN')
team.Inserir(jog1)
team.Inserir(jog2)
team.Inserir(jog3)

print(team.Listar())
print(team.Artilheiro())
print(team)

class UI:
    @staticmethod
    def menu():
        print('1 - Criar time; 2 - Inserir jogador; 3 - Listar jogadores; 4 - Mostrar artlheiro; 5 - Fim.')
        return int(input('Escolha uma opção: '))
    @staticmethod
    def main():
        op = 0
        while op != 5:
            op = UI.menu()
            if op == 1: time = UI.novo_time()
            if op == 2: UI.inserir_jogador(time)
            if op == 3: UI.listar_jogadores(time)
            if op == 4: UI.mostrar_artilheiro(time)
    @staticmethod
    def novo_time():
        nome = input('Nome do time: ')
        estado = input('Estado no qual é sediado: ')
        time = Time(nome, estado)
        return time
    def inserir_jogador(time):
        nome = input('Nome do jogador: ')
        camisa = int(input('Camisa do jogador: '))
        gols = int(input('Gols do jogador: '))
        j = Jogador(nome, camisa, gols)
        time.Inserir(j)
    def listar_jogadores():
        
UI.main()