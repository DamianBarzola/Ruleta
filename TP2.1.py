#Se pide programar al menos dos generadores de números pseudoaleatorios en particular el generador GCL del cual
#se debe testear con al menos cuatro pruebas para determinar la calidad de generación. También se pide comparar los
#generadores programados con otros, incluyendo el que posee el lenguaje Python

#https://tereom.github.io/est-computacional-2018/numeros-pseudoaleatorios.html

import numpy as np
import random as rand

from scipy.stats import chi2


semilla = 10


def GenMedio(intervalo):
    x = semilla
    if len(str(x)) > 4:
        x = x[:4]
    while len(str(x)) < 4:
        x = int(str(x)+"1")
    while True:
        square = x * x
        if len(str(square)) < 8:
            need = 8 - len(str(square))
            addZero = ""
            for j in range(0,need):
                addZero = str(0) + addZero
            square = addZero + str(square)
        else:
            square = str(square)
        x = int(square[2] + square[3] + square[4] + square[5])
        yield x


def GenGCL( intervalo):
    a, b = intervalo[0], intervalo[1]
    # parameters as in GNU C Library
    a = 54321 #Multiplicador
    c = 44498 #Incremento
    m = 2**32 #Modulo
    xi = semilla
    while True:
        xf = (a * xi + c) % m
        xi = xf
        yield int((b - a) * (xf / (m - 1)) + a)


def DatosGCL(n, intervalo):
    lista = []
    gen = GenGCL(intervalo)
    for i in range(n):
        sig = next(gen)
        lista.append(int(sig))
    return lista


def DatosMedio(n, intervalo):
    lista = []
    gen = GenMedio(intervalo)
    for i in range(n):
        sig = next(gen)
        lista.append(int(sig))
    return lista

def DatosRandint(n, rango):
    np.random.seed(semilla)
    array = []
    for i in range(n):
        array.append(np.random.randint(rango[0], rango[1]))
    return array

def main():
    rango = [1, 100]
    print(DatosGCL(50,rango))
    print(DatosRandint(50,rango))
    print(DatosMedio(50,rango))


main()
