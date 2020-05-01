#Apostaremos con el metodo D´Alembert en la ruleta y cada vez que perdamos apostaremos una ficha mas
#si ganamos volvemos a la apuesta anterior jugada
import numpy as np
from random import randint
import matplotlib.pyplot as plt
from matplotlib import ticker as tick
#condiciones iniciales
min = 0
max = 36
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36]
dineroInicial=1000
apuestaMin=10
ganadoInf=[]
ganado=[]
dineroTotalInf=[]
dineroTotal=[]


def estaencolumna():
    if randint(min, max) in numeros_rojos:
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
                apuesta=apuesta-apuestaMin
                ganado.append(1)
            else:
                dinero-=apuesta
                apuesta=apuesta+apuestaMin
                ganado.append(0)
        a+=1
    return dineroTotal


def apuestaDineroInfinito():
    tiradas=1000
    dinero=dineroInicial
    apuesta=apuestaMin

    for a in range(0,tiradas):
        dineroTotalInf.append(dinero)

        if dinero<apuesta:
            break
        else:
            if estaencolumna():
                dinero+=apuesta
                apuesta=apuestaMin - apuestaMin
                ganadoInf.append(1)
            else:
                dinero-=apuesta
                apuesta=apuesta+apuestaMin
                ganadoInf.append(0)

    return dineroTotalInf





def graficaDinero():
    calcularFrec()
    #Dinero Finito
    plt.subplot(2, 2, 1)
    plt.xlabel('Nº de tiradas')
    plt.ylabel('Cantidad de Capital')
    plt.title("Capital Acotado ")
    plt.plot([0, len(dineroTotal)], [dineroInicial, dineroInicial], color="b",label="Dinero Inicial")
    plt.plot(dineroTotal, label="Dinero",color="r")
    plt.legend()
    #Dinero Infinito
    plt.subplot(2, 2, 2)
    plt.xlabel('Nº de tiradas')
    plt.ylabel('Cantidad de Capital')
    plt.title("Capital Infinito a 1000 tiradas")
    plt.plot([0, len(dineroTotalInf)], [dineroInicial, dineroInicial], color="b",label="Dinero Inicial")
    plt.plot(dineroTotalInf, label="Dinero",color="r")
    plt.legend()
    #Frec de Aciertos acotado
    plt.subplot(2, 2, 3)
    plt.xlabel('Nº de tiradas')
    plt.ylabel('FR de Acietos')
    plt.title("Frecuencia de Aciertos con Capital Acotado")
    plt.plot(frec, color="r")
    #Frec de Aciertos inf
    plt.subplot(2, 2, 4)
    plt.xlabel('Nº de tiradas')
    plt.ylabel('FR de Acietos')
    plt.title("Frecuencia de Aciertos con Capital Infinito")
    plt.plot(frecInf, color="r")
    plt.show()



frec=[]
frecInf=[]


def calcularFrec():
    c=0
    cont=0
    b=0
    #for a in range(0,len(ganado)):
    for a in ganado:
        cont+=1
        b=b+a
        c=round(b/cont,2)
        frec.append(c)
    c=0
    cont=0
    b=0
    for a in ganadoInf:
        cont+=1
        b=b+a
        c=round(b/cont,2)
        frecInf.append(c)







def main():
    apuestaDinero()
    apuestaDineroInfinito()
    graficaDinero()



main()
