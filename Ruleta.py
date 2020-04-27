import numpy as np
from random import randint
import matplotlib.pyplot as plt
from matplotlib import ticker as tick

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
    for i in range(n):
        lista.append(randint(a,b))
        prom.append(np.mean(lista))
        promedio_promedio.append(np.mean(prom))
        desviacion.append(np.std(lista))
        desviacion_promedio.append(np.std(prom))
        if i >= 2:
            varianza.append(np.var(lista))
            varianza_promedio.append(np.var(prom))

    print("Numeros:")
    print(lista)
    Graficar(lista,prom, promedio_promedio, varianza, varianza_promedio, desviacion,desviacion_promedio)
    GraficarFrec(lista)


#--------------------------------------------------------------------------------------------------------------------




def adjust_y_axis(x, pos):
    return x / (len(lista) * 1.0)


def Graficar(lis,p, pp, v, vp, des,desp):
    #Promedio
    promEsp = np.mean(lis)
    plt.plot(list(range(len(p))), p, color="red",label="Promedio")
    plt.plot([0, n], [promEsp, promEsp], label="Promedio Esperada", color="blue")
    plt.title("Promedio")
    plt.xlabel('Nro de tiradas')
    plt.ylabel('Promedio')
    plt.legend()
    plt.show()
    #PromProm
    promEsp = np.mean(lis)
    plt.title("Promedio de los Promedios")
    plt.xlabel('Nro de tiradas')
    plt.ylabel('Promedios')
    plt.plot(pp, label="Promedio", color="red")
    plt.plot([0, n], [promEsp, promEsp], label="Promedio Esperado", color="blue")
    plt.legend()
    plt.show()
    #Varianza
    varEsp = np.var(lis)
    plt.title('Varianza')
    plt.xlabel('Nro de tiradas')
    plt.ylabel('varianza')
    plt.plot(v, label="Varianza", color="red")
    plt.plot([0, n], [varEsp, varEsp], label="Varianza Esperada", color="blue")
    plt.legend()
    plt.show()
    #VarProm
    varEsp = np.var(p)
    plt.title('Varianza de los Promedios')
    plt.xlabel('Nro de tiradas')
    plt.ylabel('varianza promedio')
    plt.plot(vp, label="Varianza", color="red")
    plt.plot([0, n], [varEsp, varEsp], label="Varianza Esperada", color="blue")
    plt.legend()
    plt.show()
    #Desviacion
    desvEsp = np.std(lis)
    plt.title('Desviacion')
    plt.xlabel('Nro de tiradas')
    plt.ylabel('desviacion')
    plt.plot(des, label="Desviacion", color="red")
    plt.plot([0, n], [desvEsp, desvEsp], label="Desviacion Esperada", color="blue")
    plt.legend()
    plt.show()
    #DesvProm
    desvPromEsp=np.std(p)
    plt.title('Desviacion de los Promedios')
    plt.xlabel('Nro de tiradas')
    plt.ylabel('desviaciones')
    plt.plot(desp, label="Desviacion", color="red")
    plt.plot([0, n], [desvPromEsp, desvPromEsp], label="Desviacion Esperada", color="blue")
    plt.legend()
    plt.show()





def GraficarFrec(lis):
    #FR
    frEsp = 1 / len(lis)
    fig, ax = plt.subplots()
    ax.hist(lis, bins=b + 1, edgecolor ="red")
    ax.yaxis.set_major_formatter(tick.FuncFormatter(adjust_y_axis))
    ax.axhline(y=frEsp * 1000, color="blue", label="Frecuencia Relativa Esperada")
    fig.tight_layout()
    plt.title("Frecuencia Relativa")
    plt.xlabel('Nro de tiradas')
    plt.ylabel('fr')
    plt.legend()
    plt.show()
    #FA
    fabsEsp = n / len(lis)
    fig, ax = plt.subplots()
    ax.hist(lis, bins=b + 1, edgecolor="red")
    ax.axhline(y=fabsEsp, color="blue", label="Frecuencia Absoluta Esperada")
    fig.tight_layout()
    plt.title("Frecuencia Absoluta")
    plt.xlabel('Nro de tiradas')
    plt.ylabel('fa')
    plt.legend()
    plt.show()



main()


#------------------------------------------------------------------------------------------------------------------------

