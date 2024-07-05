class viagem:
    def __init__(self):
        self.d = 0
        self.th = 0
        self.tm = 0

    def vel(self):
        return self.d/(self.th + self.tm/60)
    
a = viagem()

a.d = 75
a.th = 2
a.tm = 30

print(a.vel())