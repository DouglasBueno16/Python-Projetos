"""
Programa que calcula as áreas de:
    - Retângulo
    - Quadrado
    - Círculo
================================================================================================== 
class Calculadora:

    def __init__(self, area):
        self.__area = area

    def imprimir(self):
        return print('A área é {self.__area}')
==================================================================================================
"""
import math as mt

class Quadrado:  # Quadrado herda métodos de Calcula
    
    def __init__(self, lado):
        self.__lado = lado

    def calcula(self):
        self.__area = self.__lado ** 2
        return print(f'A área é {self.__area}')

class Retangulo:

    def __init__(self, lado1, lado2):
        self.__lado1 = lado1
        self.__lado2 = lado2

    def calcula(self):
        self.__area = self.__lado1 * self.__lado2
        return print(f'A área é {self.__area}')

class Circulo:
    
    def __init__(self, raio):
        self.__raio = raio

    def calcula(self):
        self.__area = mt.pi * (self.__raio ** 2)
        return print(f'A área é {self.__area}')


surpresa = input('Você deseja calcula a área de um \n 1-Quadrado \n 2-Retangulo \n 3-Circulo\n')
surpresa = int(surpresa)

if surpresa == 1:
    lado = input('Qual o lado do seu quadrado: ')
    lado = Quadrado(int(lado))
    lado.calcula()

elif surpresa == 2:
    lado1 = input('Escolha o valor de um lado: ')
    lado1 = int(lado1)
    lado2 = input('Escolha o valor do outro lado: ')
    lado2 = int(lado2)
    ret = Retangulo(lado1, lado2)
    ret.calcula()

elif surpresa == 3:
    raio = input('Qual o raio do seu círculo: ')
    raio = Circulo(int(raio))
    raio.calcula()

else:
    print('Opção inválida!')
