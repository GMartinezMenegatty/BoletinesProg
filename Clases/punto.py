import math
from abc import ABC, abstractmethod


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def aCadea(self):
        cadeaPunto = "As coordenadas son: \n\t x = "+ str(self.x) + " \n\t y = "+ str(self.y) #\n\t es para saltar de linea
        return cadeaPunto

    def distancia (self, outroPunto):
        return math.sqrt((self.x - outroPunto.x)**2 + (self.y - outroPunto.y)**2)

    def __str__(self):
        return self.aCadea()

    def __eq__(self, outro):
        return self.x == outro.x and self.y == outro.y   #comparacion


class Punto4:
    def __init__(self, x, y):
        self.x(x)
        self.y(y)

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if type(x) == int or type(x) == float:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("El valor es incorrecto")
        else:
            raise TypeError("El tipo es incorrecto")

    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("El valor es incorrecto")
        else:
            raise TypeError("El tipo de la coordenada es incorrecto")


    def Cadea(self):
        cadeaPunto = "As coordenadas son: \n\t x = "+ str(self.x) + " \n\t y = "+ str(self.y) #\n\t es para saltar de linea
        return cadeaPunto

    def __str__(self):
        return self.Cadea()

    def __eq__(self, other):
        return self.__x == other.x and self.__y == other.y

class Punto5 :
    def __init__(self, x, y):
        self.x(x)
        self.y(y)

    @property
    def y(self):
        return self.__y

    @property
    def x(self):
        return self.__x



