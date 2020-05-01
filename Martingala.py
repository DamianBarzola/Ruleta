import random as rn
import matplotlib.pyplot as plt

# aplicamos la martingala apostando al rojo hasta que que el dinero sea 0

min_n = 0
max_n = 36
numeros_rojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 20, 21, 23, 25, 27, 29, 31, 32, 34, 36]

# finito
lista_numeros = []
lista_dinero = []

# infinito
lista_numeros2 = []
lista_dinero2 = []

# iniciales
dinero_inicial = 1000
apuesta_minima = 10

frec=[]
frecInf=[]
ganadoInf=[]
ganado=[]


def getColor(numero):
    if numero in numeros_rojos:
        return "rojo"
    elif numero == 0:
        return "sin"
    else:
        return "negro"


def apuesta_dinero():
    dinero = dinero_inicial
    apuesta = apuesta_minima
    count = 0
    while dinero >= 0:
        lista_dinero.append(dinero)
        if apuesta > dinero:
            break
        lista_numeros.append(rn.randint(min_n, max_n))
        if getColor(lista_numeros[-1]) == "rojo":
            dinero += apuesta
            apuesta = apuesta_minima
            ganado.append(1)
        else:
            ganado.append(0)
            if getColor(lista_numeros[-1]) == "negro":
                dinero -= apuesta

            else:
                dinero -= apuesta / 2

            apuesta *= 2

        count += 1
    return lista_dinero


def apuesta_dineroInf():
    n=1000
    dinero = dinero_inicial
    apuesta = apuesta_minima
    for i in range(0, n):
        lista_dinero2.append(dinero)
        lista_numeros2.append(rn.randint(min_n, max_n))
        if getColor(lista_numeros2[-1]) == "rojo":
            ganadoInf.append(1)
            dinero += apuesta
            apuesta = apuesta_minima
        else:
            ganadoInf.append(0)
            if getColor(lista_numeros2[-1]) == "negro":
                dinero -= apuesta
            else:
                dinero -= apuesta / 2
            apuesta *= 2
    return lista_dinero2


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



def graficaDinero():
    calcularFrec()
    #Dinero Finito
    plt.subplot(2, 2, 1)
    plt.grid()
    plt.xlabel('Nº de tiradas')
    plt.ylabel('Cantidad de Capital')
    plt.title("Capital Acotado")
    plt.plot(lista_dinero, label="Dinero",color="r")
    plt.plot([0, len(lista_numeros)], [dinero_inicial, dinero_inicial],color="b",label="Dinero Inicial")
    plt.legend()
    #Dinero Infinito
    plt.subplot(2, 2, 2)
    plt.grid()
    plt.xlabel('Nº de tiradas')
    plt.ylabel('Cantidad de Capital')
    plt.title("Capital Infinito a 1000 tiradas")
    plt.plot(lista_dinero2, label="Dinero",color="r")
    plt.plot([0, len(lista_numeros2)], [dinero_inicial, dinero_inicial],color="b",label="Dinero Inicial")
    plt.legend()
    #Frec de Aciertos acotado
    plt.subplot(2, 2, 3)
    plt.xlabel('Nº de tiradas')
    plt.ylabel('FR de Acietos')
    plt.title("Frecuencia de Aciertos con Capital Acotado")
    plt.plot(frec,color="r")
    #Frec de Aciertos inf
    plt.subplot(2, 2, 4)
    plt.xlabel('Nº de tiradas')
    plt.ylabel('FR de Acietos')
    plt.title("Frecuencia de Aciertos con Capital Infinito")
    plt.plot(frecInf,color="r")
    plt.show()



def main():
    apuesta_dinero()
    apuesta_dineroInf()
    graficaDinero()


main()
