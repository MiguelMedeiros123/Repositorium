class circ:
    def __init__(self):
        self.r = 0
        self.pi = 3.14
    def area(self):
        return self.pi * self.r**2

a = circ()

a.r = 2

print(a.area())