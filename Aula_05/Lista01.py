#1. Um Círculo
#A classe deve ter um atributo raio para armazenar a dimensão da figura e métodos para calcular sua área e sua circunferência.
#Escrever um programa para testar a classe.

import math

# Model
class Circulo:
    def __init__(self, raio):
        self.set_raio(raio)
    def get_raio(self):
        return self.__raio
    def set_raio(self, raio):
        self.__raio = raio
        if raio < 0:
            raise ValueError()
    def calc_area(self):
        area = math.pi * self.__raio * self.__raio
        return area
    def calc_circunferencia(self):
        circ = 2 * math.pi * self.__raio
        return circ
    
# UI
circulo = Circulo(int(input('Digite o valor do raio do círculo: ')))

while True:
    x = int(input('Digite 0 para inserir outro valor de raio, 1 para saber a área do círculo, 2 para a circunferência, ou 3 para sair: '))
    
    if x == 0:
        circulo.set_raio(int(input('Digite o novo valor do raio: ')))
    elif x == 1:
        print('Área do Circulo:', circulo.calc_area())
    elif x == 2:
        print('Comprimento da Circunferência:', circulo.calc_circunferencia())
    elif x == 3:
        print('Fim do programa')
        break
    else:
        print('Opção Inválida')
