from datetime import datetime
from datetime import timedelta

class Musica:
    def __init__(self, titulo: str, artista: str, album: str, duracao: timedelta):
        if titulo != "": self.__titulo = titulo
        else: raise ValueError('Insere um título válido.')
        if artista != "": self.__artista = artista
        else: raise ValueError('Insere um artista válido.')
        if album != "": self.__album = album
        else: raise ValueError('Insere um album válido.')
        self.__dataInclusao = datetime.now()
        if duracao > timedelta(minutes=0, seconds=0): self.__duracao = duracao
        else: raise ValueError('Insere uma duração válida.')
    def getDuracao(self):
        return self.__duracao
    def __str__(self):
        return f"Título: {self.__titulo}; Artista: {self.__artista}; Álbum: {self.__album}; Data de inclusão: {self.__dataInclusao}; Duração: {self.__duracao}."

class PlayList:
    def __init__(self, nome: str, descricao: str):
        if nome != "": self.__nome = nome
        else: raise ValueError('Insere um nome válido.')
        if descricao != "": self.__descricao = descricao
        else: raise ValueError('Insere uma descrição válida.')
        self.__musicas = []
    def Inserir(self, m: Musica):
        self.__musicas.append(m)
    def Listar(self):
        l = []
        for x in self.__musicas:
            l.append(x.__str__())
        return l
    def TempoTotal(self):
        t = timedelta(seconds=0)
        for x in self.__musicas:
            t += x.getDuracao()
        return t
    def __str__(self):
        return f"Nome: {self.__nome}; Descrição: {self.__descricao}; Músicas: {self.Listar()}; Duração total: {self.TempoTotal()}."

diesirae = Musica('dies irae', 'mozart', 'requiem in d minor', timedelta(minutes=1, seconds=45))
tef = Musica('toccata e fugue', 'bach', 'bach music', timedelta(minutes=10))
print(diesirae)
print(tef)
p = PlayList('classical', 'classical music playlist')

p.Inserir(diesirae)
p.Inserir(tef)
print(p.TempoTotal())
print(p.Listar())

print(p)