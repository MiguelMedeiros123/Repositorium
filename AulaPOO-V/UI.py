from dis import dis
from triangulo import Triangulo
from corrida import Corrida


class UI:
    @staticmethod
    def menu():
        print('1 - corrida; 2 - triangulo; 3 - fim.')
        return int(input('Escolha uma opção: '))
    @staticmethod
    def main():
        op = 0
        while op != 3:
            op = UI.menu()
            if op == 1: UI.nova_corrida()
            if op == 2: UI.novo_triangulo()
    @staticmethod
    def nova_corrida():
        c = Corrida()
        distancia = float(input('Informe a distância em metros: '))
        tempo = (input("Informe o tempo no formato 'hh:mm:ss': "))
        c.set_distancia(distancia)
        c.set_tempo(tempo)
        print(f'Seu pace é de {c.pace()} min/km.\n')
    @staticmethod
    def novo_triangulo():
        t = Triangulo()
        t.set_base(float(input('Informa o valor da base: ')))
        t.set_altura(float(input('Informa o valor da altura: ')))
        print(f'A área do triângulo é {t.calc_area()} u.a.\n')

UI.main()