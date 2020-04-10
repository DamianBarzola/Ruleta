import numpy as np
import matplotlib.pyplot as mat

#np.mean()promedio  np.dev desviacion   np.var varianza
a=0
b=36


def ruleta(a,b,n):
    return np.random.randint(a, b, n)


def cant(a,Lista):
    c=0
    for i in Lista:
        if(a==i):
            c=c+1
    return c


def calcFR(Lista):
    FrecR=[]
    lista_nueva = []
    for i in Lista:
        z=(cant(i,Lista)/len(Lista))
        if i not in lista_nueva:
            lista_nueva.append(i)
            FrecR.append(z)
    return FrecR



def main():
    n=int(input("Ingrese numero de muestras: "))
    Lista=ruleta(a,b,n)
    print(Lista)
    TablaFrec(Lista)
    TablaProm(Lista)


def TablaProm(Lista):
    z=[]
    x=np.mean(Lista)
    for i in Lista:
        z.append(x)
    mat.plot(Lista,z)
    mat.show()
    


def TablaFrec(Lista):
    FR=calcFR(Lista)
    frEsp=[]
    for i in FR:
        frEsp.append(1/37)
    mat.plot(FR,"r")
    mat.plot(frEsp,"b")
    mat.xlabel("Nros Diferentes de la ruleta")
    mat.ylabel("Frecuencia Relativa")
    mat.show()


main()

#------------------------------------------------------------------------------------------------------------------------


from random import randint
import matplotlib.pyplot as plt
from matplotlib import ticker as tick
import statistics

#https://www.overleaf.com/project/5c9b84ff1e4a775dfb31fc34

n_muestras = 100
min_n = 0
max_n = 36

data = []
promedio = []
promedio_promedio = []
varianza = []
varianza_media = []

def adjust_y_axis(x, pos):
    return x / (len(data) * 1.0)

def plot(a,p,pp,v,vm):

	#graficar histograma de frecuencias absolutas

	fig, ax = plt.subplots()
	n, bins, patches = ax.hist(a, bins = max_n+1)
	fig.tight_layout()
	plt.title("Histograma de frecuencia absoluta")
	plt.show()


	#graficar histograma frecuencia relativa
	fig, ax = plt.subplots()
	n, bins, patches = ax.hist(a, bins = max_n+1)
	fig.tight_layout()
	plt.title("Histograma de frecuencia relativa")
	ax.yaxis.set_major_formatter(tick.FuncFormatter(adjust_y_axis))
	plt.show()


	#graficar media
	plt.plot(list(range(len(p))), p, color='b')
	plt.title("Media")
	plt.show()

	#graficar media de media
	plt.plot(list(range(len(pp))), pp, color='b')
	plt.title("Media de las medias")
	plt.show()

	#graficar varianza
	plt.plot(list(range(len(v))), v, color='b')
	plt.title("Varianza")
	plt.show()

	#graficar varianza de media
	plt.plot(list(range(len(vm))), vm, color='b')
	plt.title("Varianza de las medias")
	plt.show()


def showarr(a):
	for i in range(min_n, max_n+1):
		print(str(i) + ": "+str(a.count(i)))


for i in range(n_muestras):
	data.append(randint(min_n,max_n))
	promedio.append(statistics.mean(data))
	promedio_promedio.append(statistics.mean(promedio))
	if i >= 2:
		varianza.append(statistics.variance(data))
		varianza_media.append(statistics.variance(promedio))


plot(data,promedio,promedio_promedio,varianza,varianza_media)
showarr(data)

#

