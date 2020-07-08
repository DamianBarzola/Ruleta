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
lamda = 0.80 #clientes por minuto
mu = 1
total_cus = 50


def inicializar():
    global limCola, ocupado, desocup, reloj, tipoEventoSig, estado, cliEnCola, nroTEvento, cliCompletaronDemora, area_cliEnCola, area_estado, arriboTiempo, ultEventoTiempo, sigEventoTiempo, DemorasTotal
    limCola = 100000
    ocupado = 1    #ocupado
    desocup = 0    #desocupado
    reloj = 0     #reloj del simulacion
    tipoEventoSig = 0    #tipo de evento siguiente
    estado = desocup    #estado del servidor
    cliEnCola = 0    #num de clientes actualmente en cola
    nroTEvento = 2      #num de tipos de eventos
    cliCompletaronDemora = 0     #num de clientes que completaron demora
    area_cliEnCola = 0.0         #area debajo de Q(t)
    area_estado = 0.0    #area debajo de B(t)
    ultEventoTiempo= 0.0   #tiempo del ultimo evento
    sigEventoTiempo = [ 0, reloj + generarU((1/lamda)), 1e30]  #tiempo del siguiente evento de tipo 1 o 2
    arriboTiempo = []    #tiempo de arrivo de clientes a la cola
    DemorasTotal = 0   #total de demoras completadas

def generarU(a):
    u = random.random()
    x = -a * math.log(u)
    return x

def timing():
    global tipoEventoSig, sigEventoTiempo, reloj, min_sigEventoTiempo, nroTEvento
    min_sigEventoTiempo = 1e29  #tiempo minimo del siguiente evento
    tipoEventoSig = 0    #0 si no hay otro evento
    for i in range(1, nroTEvento+1):
        if sigEventoTiempo[i] < min_sigEventoTiempo:
            min_sigEventoTiempo = sigEventoTiempo[i]
            tipoEventoSig = i
    if tipoEventoSig == 0:
        print("Lista vacia en tiempo %f" % reloj)
        return 1
    else:
        reloj = min_sigEventoTiempo
        return 0

def arribo():
    global sigEventoTiempo, reloj, lamda, estado, cliEnCola, cliCompletaronDemora, mu, DemorasTotal
    sigEventoTiempo[1] = reloj + generarU(1/lamda)
    if estado == ocupado:
        cliEnCola += 1
        arriboTiempo.append(reloj)
    else:
        # delay = 0
        # DemorasTotal += delay
        cliCompletaronDemora += 1
        estado = ocupado
        sigEventoTiempo[2] = reloj + generarU(1/mu)


def salida():
    global cliEnCola, estado, sigEventoTiempo, DemorasTotal, arriboTiempo, cliCompletaronDemora, mu
    if cliEnCola == 0:
        estado = desocup
        sigEventoTiempo[2] = 1e30
    else:
        delay = reloj - arriboTiempo.pop(0)
        DemorasTotal += delay
        cliEnCola -= 1
        cliCompletaronDemora += 1
        sigEventoTiempo[2] = reloj + generarU(1/mu)


def main():
    global ultEventoTiempo,area_cliEnCola,area_estado
    util_corridas, avgdel_corridas, avgniq_corridas, time_corridas = [], [], [], []     #guardo los rdos de cada corrida para sacar los proms

    print("Parametros: ")
    print("Tiempo medio entre arribos: %.3f minutos" % (1/lamda))
    print("Tiempo medio de servicio: %.3f minutos" % (1/mu))
    print("Tasa de arribo: %.2f " % ((1/lamda)/(1/mu)*100)+ "%")
    print("Clientes en el sistema: %d" % total_cus)

    for i in range(10):
        inicializar()
        time_acum, server_acum, niq_acum = [], [], []
        while cliCompletaronDemora < total_cus:
            t = timing()
            if t == 0:
            # update_time_avg_stats()
                time_since_last_event = reloj - ultEventoTiempo
                ultEventoTiempo= reloj
                area_cliEnCola = area_cliEnCola + (cliEnCola * time_since_last_event)
                area_estado = area_estado + (estado * time_since_last_event)
                time_acum.append(reloj)
                server_acum.append(estado)
                niq_acum.append(cliEnCola)

                if tipoEventoSig == 1:
                    arribo()
                elif tipoEventoSig == 2:
                    salida()

            elif t == 1:
                break

        util_corridas.append(area_estado / reloj)
        avgdel_corridas.append(DemorasTotal / cliCompletaronDemora)
        avgniq_corridas.append(area_cliEnCola / reloj)
        time_corridas.append(reloj)
        print("\nCorrida %d: " % (i+1))
        print("Tiempo promedio de cliente en cola: %.3f minutos " % (DemorasTotal / cliCompletaronDemora))
        print("Promedio de clientes en cola: %.3f" % (area_cliEnCola / reloj))
        print("Utilizacion del servidor: %.3f " % (area_estado / reloj))
        print("Tiempo total: %.3f" % reloj)

    print("\nPromedios de los 10 reportes: ")
    print("Promedio de tiempos promedios de clientes en cola: %.3f" % np.mean(avgdel_corridas))
    print("Promedio de promedios de clientes en cola:  %.3f" % np.mean(avgniq_corridas))
    print("Promedios de utilidad del servidor: %.3f" % np.mean(util_corridas))
    print("Promedio de tiempo total: %.3f" % np.mean(time_corridas))

main()
