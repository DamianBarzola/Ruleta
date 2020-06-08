#Se pide programar al menos dos generadores de números pseudoaleatorios en particular el generador GCL del cual
#se debe testear con al menos cuatro pruebas para determinar la calidad de generación. También se pide comparar los
#generadores programados con otros, incluyendo el que posee el lenguaje Python

#https://tereom.github.io/est-computacional-2018/numeros-pseudoaleatorios.html
import math
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
    a = 54321
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
    u=[]
    for i in range(15000):
        u.append(rand.random())
    return u


def testChi(u,n):
    print("Test de Chi2")
    a=[]
    b=1500
    c=0.1
    for i in range (n):
        x =0
        for j in range (len(u)):
            if  (c-0.1)<=float(u[j])<=c:
                x+=1
        a.append(x)
        c+=0.1
    x2=0
    for i in range(len(a)):
        x2+=(((a[i]-b)**2)/b)
    print("X2 = "+ str(x2))


def testCorridas(u):
    print("Test Corridas:")
    lista = []
    cont = 1
    for i in range(len(u)-1):
        if u[i+1] >= u[i]:
            lista.append("+")
        else:
            lista.append("-")

    for i in range(1, len(lista)):
        if (lista[i] != lista[i-1]):
            cont += 1
    n = len(lista)
    media = (2*n-1)/3
    desv = math.sqrt((16*n-29)/90)
    z = (cont-media)/desv
    print("Z= "+ str(z))


def main():
    rango = [1, 100]
    a=DatosGCL(50,rango)
    b=DatosRandint(50,rango)
    c=DatosMedio(50,rango)
    print(a)
    print(b)
    print(c)
    testCorridas(a)
    testCorridas(b)
    testCorridas(c)
    testChi(a,50)
    testChi(b,50)
    testChi(c,50)



main()
