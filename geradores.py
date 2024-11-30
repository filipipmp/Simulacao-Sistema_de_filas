import math

class Gerador_Aleatorio:
    def __init__(self, seed = 11, a = 16807, c = 0, m = 2147483647):
        self.seed, self.a, self.c, self.m, self.Xn = seed, a, c, m, seed
        self.random()
        self.random()
        
    def random(self):
        self.Xn = (self.a*self.Xn + self.c) % self.m
        return self.Xn/self.m

class Gerador_TEC:
    def __init__(self, gerador_base):
        self.gerador_base = gerador_base
    
    def random(self):
        return -15*math.log(self.gerador_base.random())

class Gerador_TS:
    def __init__(self, gerador_base):
        self.gerador_base = gerador_base
    
    def random(self, tipo):
        if (tipo == 1):
            return  -15*math.log(self.gerador_base.random()) + 15
        if (tipo == 2):
            return  -40*math.log(self.gerador_base.random()) + 30
        if (tipo == 3):
            return -140*math.log(self.gerador_base.random()) + 60
