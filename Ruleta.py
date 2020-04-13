import numpy as np
from random import randint
import matplotlib.pyplot as plt
from matplotlib import ticker as tick
import statistics

#np.mean()promedio  np.std desviacion   statistics.variance varianza
n=1000
a=0
b=36
prom = []
promedio_promedio = []
varianza = []
varianza_promedio = []
FrecR=[]
desviacion = []
desviacion_promedio = []
lista=[]


def main():
    Listas()
    print("Numeros:")
    print(lista)
    TablaProm()
    TablaPromProm()
    TablaFrecRel()
    TablaFrecAbs()
    TablaVarianza()
    TablaVarProm()
    TablaDesviacion()
    TablaDesvProm()


#--------------------------------------------------------------------------------------------------------------------

def Listas():
    for i in range(n):
        lista.append(randint(a,b))
        prom.append(statistics.mean(lista))
        promedio_promedio.append(statistics.mean(prom))
        desviacion.append(np.std(lista))
        desviacion_promedio.append(np.std(prom))
        if i >= 2:
            varianza.append(statistics.variance(lista))
            varianza_promedio.append(statistics.variance(prom))


def adjust_y_axis(x, pos):
    return x / (len(lista) * 1.0)


def TablaProm():
    promEsp = np.mean(lista)
    plt.plot(list(range(len(prom))), prom, color="red",label="Promedio")
    plt.plot([0, n], [promEsp, promEsp], label="Promedio Esperada", color="blue")
    plt.title("Promedio")
    plt.xlabel('Nro de tiradas')
    plt.ylabel('Promedio')
    plt.legend()
    plt.show()


def TablaPromProm():
    promEsp = np.mean(lista)
    plt.title("Promedio de los Promedios")
    plt.xlabel('Nro de tiradas')
    plt.ylabel('Promedios')
    plt.plot(promedio_promedio, label="Promedio", color="red")
    plt.plot([0, n], [promEsp, promEsp], label="Promedio Esperado", color="blue")
    plt.legend()
    plt.show()


def TablaFrecRel():
    frEsp = 1 / len(lista)
    fig, ax = plt.subplots()
    ax.hist(lista, bins=b + 1, edgecolor ="red")
    ax.yaxis.set_major_formatter(tick.FuncFormatter(adjust_y_axis))
    ax.axhline(y=frEsp * 1000, color="blue", label="Frecuencia Relativa Esperada")
    fig.tight_layout()
    plt.title("Frecuencia Relativa")
    plt.xlabel('Nro de tiradas')
    plt.ylabel('fr')
    plt.legend()
    plt.show()


def TablaFrecAbs():
    fabsEsp = n / len(lista)
    fig, ax = plt.subplots()
    ax.hist(lista, bins=b + 1, edgecolor="red")
    ax.axhline(y=fabsEsp, color="blue", label="Frecuencia Absoluta Esperada")
    fig.tight_layout()
    plt.title("Frecuencia Absoluta")
    plt.xlabel('Nro de tiradas')
    plt.ylabel('fa')
    plt.legend()
    plt.show()


def TablaVarianza():
    varEsp = np.var(lista)
    plt.title('Varianza')
    plt.xlabel('Nro de tiradas')
    plt.ylabel('varianza')
    plt.plot(varianza, label="Varianza", color="red")
    plt.plot([0, n], [varEsp, varEsp], label="Varianza Esperada", color="blue")
    plt.legend()
    plt.show()


def TablaVarProm():
    varEsp = np.var(lista)
    plt.title('Varianza de los Promedios')
    plt.xlabel('Nro de tiradas')
    plt.ylabel('varianza promedio')
    plt.plot(varianza_promedio, label="Varianza", color="red")
    plt.plot([0, n], [varEsp, varEsp], label="Varianza Esperada", color="blue")
    plt.legend()
    plt.show()


def TablaDesviacion():
    desvEsp = np.std(lista)
    plt.title('Desviacion')
    plt.xlabel('Nro de tiradas')
    plt.ylabel('desviacion')
    plt.plot(desviacion, label="Desviacion", color="red")
    plt.plot([0, n], [desvEsp, desvEsp], label="Desviacion Esperada", color="blue")
    plt.legend()
    plt.show()


def TablaDesvProm():
    desvPromEsp=np.std(prom)
    plt.title('Desviacion de los Promedios')
    plt.xlabel('Nro de tiradas')
    plt.ylabel('desviaciones')
    plt.plot(desviacion_promedio, label="Desviacion", color="red")
    plt.plot([0, n], [desvPromEsp, desvPromEsp], label="Desviacion Esperada", color="blue")
    plt.legend()
    plt.show()


main()

#------------------------------------------------------------------------------------------------------------------------

