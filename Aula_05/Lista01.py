import math

class Circulo:
    def __init__(self):
        self.raio = 0
    def calc_area(self):
        area = math.pi * self.raio * self.raio
        return area
    def calc_circunferencia(self):
        circ = 2 * math.pi * self.raio
        return circ
    
# main:
circulo = Circulo()

circulo.raio = int(input('Digite o valor do raio do círculo: '))

while True:
    x = int(input('Digite 0 para inserir outro valor de raio, 1 para saber a área do círculo, 2 para a circunferência, ou 3 para sair: '))
    
    if x == 0:
        circulo.raio = int(input('Digite o novo valor do raio: '))
    elif x == 1:
        print('Área do Circulo:', circulo.calc_area())
    elif x == 2:
        print('Comprimento da Circunferência:', circulo.calc_circunferencia())
    elif x == 3:
        print('Fim do programa')
        break
    else:
        print('Opção Inválida')