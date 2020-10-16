import math

"""
***************************************************************
@@ ejercicio 1 @@
un metodo python que haga la suma de 2 numeros
2+4 = 6
"""


# start-->
def suma():
    suma=2+4
    return suma


"""
***************************************************************
@@ ejercicio 2 @@
la suma de los numeros pares del 1 al 1000
"""


# start-->
def sumaPares():
    resultado = 0
    i = 0
    while i <= 1000:
        if (i%2==0):
            resultado = resultado + i
        i = i+1
    return resultado


"""
***************************************************************
@@ ejercicio 3 @@
encontrar el area total de superficie de un cilindro
radio = 5 m
altura = 7 m
area lateral: 2*pi*r*a
area circulo: 2*pi*r^2
area total: area lateral + area circulo
"""


# start-->
def areaTotalCilindro():
    areaTotal= round((areaLateral()+areaCirculo()),2)
    return areaTotal


def areaLateral():
    radio = 5.0 
    altura = 7.0 
    areaLateral = (2.0 * math.pi * radio * altura)
    return areaLateral


def areaCirculo():
    radio = 5.0 
    areaCirculo = (2.0*math.pi*radio**2)
    return areaCirculo


"""
***************************************************************
@@ ejercicio 4 @@
el ejercicio numero 3 convertirlo en una clase

"""
        
# start-->
class Cilindro:
    def areaTotalCilindro(self):
        radio = 5.0
        haltura = 7.0
        area = round((2*math.pi*radio**2 + 2*math.pi*radio*altura), 2)
        return area


"""
***************************************************************
@@ ejercicio 5 @@
restaurante de pizzas
pizza
    nombre
    lugar
    costo
    conDescuento
    descuento
"""


class Restaurante:
    
    listaOrdenes = []
    costoTotal = 0
    DescuentoTotal = 0

    def ordenar(self,Pizza()):

        self.Pizza()=ordenar

        orden = dict(ordenar)


    def costoTotal(self):
        for orden in listaOrdenes:
            costoT=listaOrdenes[2]
            costoTotal =  costoTotal + costoT
        return costoTotal

    def costoTotalConDescuento(self):
        for orden in listaOrdenes:
            Descuento=listaOrdenes[4]
            DescuentoTotal = DescuentoTotal + Descuento
        costoTotalConDescuento = costoTotal()-DescuentoTotal
        return costoTotalConDescuento


class Pizza:
    def __init__(self,nombre,lugar,costo,conDescuento,descuento):
        self.nombre=nombre
        self.lugar=lugar
        self.costo=costo
        self.conDescuento=conDescuelto
        self.descuelto=descuento


"""
***************************************************************
@@ ejercicio 6 @@
colocar este proyecto en github
colocar aca debajo la url
ademas colocar la url en un archivo
github_<nombre>_<codigo>.txt y subirlo a moodle
"""


# github url-->
def getGithubUrl():
    return ""
