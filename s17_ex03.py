"""
Quadrado - Calcular
    -Área
    -Perímetro
    -Imprimir dados

quad = Quadrado(4)
quad.area()
quad.perimetro()
quad.imprimir()    
"""

class Quadrado:

    def __init__(self, lado):
        self.__lado = lado
    
    def area(self):
        self.__ar = self.__lado ** 2
        # return f'A área do quadrado é {self.__lado ** 2}' 

    def perimetro(self):
       self.__per = self.__lado * 4
       # return f'O perímetro do quadrado é {4*self.__lado}'

    def imprimir(self):
        return print(f'O perímetro é: {self.__per} \n A área é: {self.__ar}')

quad = input('Qual o lado do quadrado? ')
quad = Quadrado(int(quad))

quad.area()
quad.perimetro()
quad.imprimir()