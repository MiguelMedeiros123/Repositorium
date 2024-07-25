class Retangulo:
    def __init__init(self, base, altura):
        if base > 0: self.__base = self.set_base(base)
        else: raise ValueError("Insere uma base maior que zero.")

        if altura > 0: self.__altura = altura
        else: raise ValueError("Insere uma altura maior que zero.")