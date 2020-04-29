#Apostaremos a 1 de las tres columnas de la ruleta y cada vez que perdamos apostaremos una ficha mas
#si ganamos volvemos a la apuesta inicial
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from matplotlib import ticker as tick
#condiciones iniciales
min = 0
max = 36
columna1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
dineroInicial=1000
apuestaMin=10
ganadoInf=[]
ganado=[]
dineroTotalInf=[]
dineroTotal=[]


def estaencolumna():
    if randint(min, max) in columna1:
        return True
    else:
        return False


def apuestaDinero():
    dinero=dineroInicial
    apuesta=apuestaMin
    a=0

    while dinero>=0:
        dineroTotal.append(dinero)
        if dinero<apuesta:
            break
        else:
            if estaencolumna():
                dinero+=apuesta
                apuesta=apuestaMin
            else:
                dinero-=apuestaMin
                apuesta=apuestaMin+10
        a+=1
    return dineroTotal


def apuestaDineroInfinito():
    tiradas=1000
    dinero=dineroInicial
    apuesta=apuestaMin

    for a in range(0,tiradas):
        dineroTotalInf.append(dinero)
        if estaencolumna():
            dinero+=apuesta
            apuesta=apuestaMin

        else:
            dinero-=apuestaMin
            apuesta=apuestaMin+10

    return dineroTotalInf





def graficaDinero():
    #Dinero Finito
    plt.subplot(2, 2, 1)
    plt.xlabel('Nº de tiradas')
    plt.ylabel('Cantidad de Calidad')
    plt.title("1de3 ")
    plt.plot([0, len(dineroTotal)], [dineroInicial, dineroInicial], color="b",label="Dinero Inicial")
    plt.plot(dineroTotal, label="flujo de dinero",color="r")
    plt.legend()
    #Dinero Infinito
    plt.subplot(2, 2, 2)
    plt.xlabel('Nº de tiradas')
    plt.ylabel('Cantidad de Calidad')
    plt.title("1de3 con dinero infinito")
    plt.plot([0, len(dineroTotalInf)], [dineroInicial, dineroInicial], color="b",label="Dinero Inicial")
    plt.plot(dineroTotalInf, label="flujo de dinero",color="r")
    plt.legend()
    plt.show()



def main():
    apuestaDinero()
    apuestaDineroInfinito()
    graficaDinero()



main()
