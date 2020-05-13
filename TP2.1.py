#Se pide programar al menos dos generadores de números pseudoaleatorios en particular el generador GCL del cual
#se debe testear con al menos cuatro pruebas para determinar la calidad de generación. También se pide comparar los
#generadores programados con otros, incluyendo el que posee el lenguaje Python.
#A modo de introducción y ejemplos de código se deja un link en la sección de Recursos online obligatorios

#https://tereom.github.io/est-computacional-2018/numeros-pseudoaleatorios.html

#Algunos metodos en video
#https://www.youtube.com/watch?v=2EqFYmpCnm8
import sys


def main():
    pass


semillas=[]
valor=[]
def centrodelcuadrado(semilla,n):       #esta mal
    semillas.append(n)
    valor.append(n)
    for a in range(0,n):
        x=semilla*semilla
        if(sys.getsizeof(int(x))<2):
            x=(x/1e2)%1e4
        else:
            x=0
        valor.append(x)
        semillas.append(semilla)
    return valor





main()
