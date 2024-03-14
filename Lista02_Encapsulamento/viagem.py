#2 - Uma Viagem
#Escrever a classe Viagem de acordo com o diagrama UML apresentado abaixo. A classe deve ter atributos para
#armazenar a distância em km e o tempo gasto em horas e minutos da viagem realizada. A classe deve possuir
#método para calcular a velocidade média atingida na viagem em km/h de acordo com a distância e o tempo gasto,
#além dos métodos de acesso para definir e recuperar os atributos.
#Escrever um programa para testar a classe.

class Viagem:
    def __init__(self):
        self.__distancia = 0
        self.__tempo = 0
    def get_distancia(self):
        return self.__distancia
    def set_distancia(self, distancia):
        self.__distancia = distancia
        if distancia < 0: raise ValueError()
    def get_tempo(self):
        return self.__tempo
    def set_tempo(self, tempo):
        self.__tempo = tempo
        if tempo < 0: raise ValueError()
    def velocidade_media(self):
        vel = self.__distancia / self.__tempo
        return vel

class UI:
    @staticmethod
    def main():
        v = Viagem()
        
        v.set_distancia(float(input('Digite o valor da distância em KM: ')))
        v.set_tempo(float(input('Digite o valor do tempo percorrido em horas: ')))

        while True:
            x = float(input('Digite 0 para inserir outro valor para a distância, 1 para inserir outro valor de tempo, 2 para calcular a velocidade média, ou 3 para sair: '))
            
            if x == 0:
                v.set_distancia(float(input('Digite o novo valor da distância em KM: ')))
            elif x == 1:
                v.set_tempo(float(input('Digite o novo valor do tempo em horas: ')))
            elif x == 2:
                print('Velocidade Média:', v.velocidade_media())
            elif x == 3:
                print('Fim do programa')
                break
            else:
                print('Opção Inválida')
                
UI.main()
