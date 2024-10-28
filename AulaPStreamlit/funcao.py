class Funcao:
    def __init__(self, a: float, b: float, c: float) -> None:
        self.a = a
        self.b = b
        self.c = c
    
    def __str__(self) -> str:
        if self.a != 1: y = (f"{self.a}x^2 ")
        else: y = "x^2"
        if self.b > 0: y += (f"+{self.b}x ")
        elif self.b < 0: y += (f"{self.b}x ")
        if self.c > 0: y += (f"+{self.c}")
        elif self.c < 0: y += (f"{self.c}")
        return y
    def delta(self):
        return self.b**2 - 4*self.a*self.c

    def xv(self):
        return (-1*self.b)/(2*self.a)
    
    def yv(self):
        return self.f(self.xv())
    
    def x1(self):
        return (-1*self.b - self.delta()**(1/2))/(2*self.a)
    
    def x2(self):
        return (-1*self.b + self.delta()**(1/2))/(2*self.a)
    
    def f(self, x: int):
        return self.a*(x**2) + self.b*x + self.c