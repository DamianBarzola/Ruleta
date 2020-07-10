#
#Se solicita realizar un estudio de Simulación de un sistema MM1 que tenga al menos los siguientes análisis:

#+ Medidas de Rendimiento:

#- Promedio de clientes en el sistema.
#- Promedio de clientes en cola.
#- Tiempo promedio en sistema.
#- Tiempo promedio en cola.
#- Utilización del servidor.
#- Probabilidad de n clientes en cola.
#- Probabilidad de denegación de servicio (cola finita de tamaño: 0, 2, 5, 10, 50).

#+ Tasas de arribo: 25%, 50%, 75%, 100%, 125% con respecto a la tasa de servicio.

#+ 10 corridas por cada experimento.

#+ Gráficas y análisis correspondientes a cada caso. No olvidar agregar marcó teórico y fórmulas.

#+ Comparar los resultados de las tres fuentes de datos: el valor teórico esperado, programa en Python e implementación en Anylogic.

import random
import math
import sys
import numpy as np
import matplotlib.pyplot as plt

#Variables Globales

n = 50
def inicializar(lamda):
    global limCola, ocupado, desocup, reloj, tipoEventoSig, estado, cliEnCola, nroTEvento, cliCompletaronDemora, area_cliEnCola, area_estado, arriboTiempo, ultEventoTiempo, sigEventoTiempo, DemorasTotal
    limCola = 100000
    reloj = 0
    tipoEventoSig = 0
    estado = True
    cliEnCola = 0
    nroTEvento = 2
    cliCompletaronDemora = 0
    area_cliEnCola = 0.0
    area_estado = 0.0
    ultEventoTiempo= 0.0
    sigEventoTiempo = [ 0, reloj + generarU((1/lamda)), 1e30]
    arriboTiempo = []
    DemorasTotal = 0

def generarU(a):
    u = random.random()
    x = -a * math.log(u)
    return x

def timing():
    global tipoEventoSig, sigEventoTiempo, reloj, min_sigEventoTiempo, nroTEvento
    min_sigEventoTiempo = 1e29
    tipoEventoSig = 0
    for i in range(1, nroTEvento+1):
        if sigEventoTiempo[i] < min_sigEventoTiempo:
            min_sigEventoTiempo = sigEventoTiempo[i]
            tipoEventoSig = i
    if tipoEventoSig == 0:
        return 1
    else:
        reloj = min_sigEventoTiempo
        return 0

def arribo(mu,lamda):
    global sigEventoTiempo, reloj, estado, cliEnCola, cliCompletaronDemora,  DemorasTotal
    sigEventoTiempo[1] = reloj + generarU(1/lamda)
    if estado == False:
        cliEnCola += 1
        arriboTiempo.append(reloj)
    else:
        # delay = 0
        # DemorasTotal += delay
        cliCompletaronDemora += 1
        estado = False
        sigEventoTiempo[2] = reloj + generarU(1/mu)


def salida(mu):
    global cliEnCola, estado, sigEventoTiempo, DemorasTotal, arriboTiempo, cliCompletaronDemora
    if cliEnCola == 0:
        estado = True
        sigEventoTiempo[2] = 1e30
    else:
        delay = reloj - arriboTiempo.pop(0)
        DemorasTotal += delay
        cliEnCola -= 1
        cliCompletaronDemora += 1
        sigEventoTiempo[2] = reloj + generarU(1/mu)


def main(mu):
    lamda = 1
    global ultEventoTiempo,area_cliEnCola,area_estado
    util_corridas, avgdel_corridas, avgniq_corridas, time_corridas = [], [], [], []
    print("Parametros: ")
    print("Tiempo medio entre arribos: %.3f minutos" % (1/lamda))
    print("Tiempo medio de servicio: %.3f minutos" % (1/mu))
    print("Tasa de arribo: %.2f " % ((lamda/mu)*100)+ "%")
    print("Clientes en el sistema: ", n)

    for i in range(10):
        inicializar(lamda)
        time_acum, server_acum, niq_acum = [], [], []
        while cliCompletaronDemora < n:
            t = timing()
            if t == 0:
                time_since_last_event = reloj - ultEventoTiempo
                ultEventoTiempo= reloj
                area_cliEnCola = area_cliEnCola + (cliEnCola * time_since_last_event)
                area_estado = area_estado + (estado * time_since_last_event)
                time_acum.append(reloj)
                server_acum.append(estado)
                niq_acum.append(cliEnCola)

                if tipoEventoSig == 1:
                    arribo(mu,lamda)
                elif tipoEventoSig == 2:
                    salida(mu)

            elif t == 1:
                break

        util_corridas.append(area_estado / reloj)
        avgdel_corridas.append(DemorasTotal / cliCompletaronDemora)
        avgniq_corridas.append(area_cliEnCola / reloj)
        time_corridas.append(reloj)

    print("\nPromedios de las 10 corridas con tasa de arribo: %.2f " % ((lamda/mu)*100)+ "%")
    print("Promedio de tiempos promedios de clientes en cola: %.3f" % np.mean(avgdel_corridas))
    print("Promedio de promedios de clientes en cola:  %.3f" % np.mean(avgniq_corridas))
    print("Promedios de utilidad del servidor: %.3f" % (1-np.mean(util_corridas)))
    print("Promedio de tiempo total: %.3f" % np.mean(time_corridas))
    print("\n-------------------------------------------------------------------------------------------------------------- ")


a=(12/9)
m=[4,2,a,1,0.8]
for i in m:
    main(i)
