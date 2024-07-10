import math

class Retangulo:
    def __init__(self, b, h):
        self.set_base(b)
        self.set_altura(h)
    def set_base(self, b):
        if b > 0: self.__b = b
        else: raise ValueError()
    def set_altura(self, h):
        if h > 0: self.__h = h
        else: raise ValueError()
    def get_base(self):
        return self.__b
    def get_altura(self):
        return self.__h
    def calc_area(self):
        return self.get_altura() * self.get_base()
    def calc_diagonal(self):
        return math.sqrt(self.get_base() ** 2 + self.get_altura() ** 2)
    def __str__(self):
        return f'base = {self.get_base()} altura = {self.get_altura()}'
    
class UI:
    @staticmethod
    def main():
        b = float(input('digite a base do retangulo: '))
        h = float(input('digite a altura do retangulo: '))
        r = Retangulo(b,h)
        print(r)
        print(r.get_base())
        print(r.get_altura())
        print(f'área do retangulo = {r.calc_area()}')
        print(f'diagonal do retangulo = {r.calc_diagonal()}')
        
UI.main()