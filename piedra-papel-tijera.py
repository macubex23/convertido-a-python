import math
from random import random

from more_itertools import numeric_range


def alea(min, max):
    numero = math.floor(random() * (max - min + 1) + min)
    return numero

piedra = 0
papel = 1
tijera = 2

opciones = ["piedra","papel","tijera"]

opcionUsuario = int(input("¿Que elijes?\npiedra:\t0 \nPapel:\t1 \nTijera:\t2 " + "\n" ))
opcionMaquina = alea(0,2)

if(opcionUsuario == piedra):
    if(opcionMaquina == piedra):
        print("empate")
    elif (opcionMaquina == papel):
        print("perdiste")
    elif (opcionMaquina == tijera):
        print("ganaste")
elif (opcionUsuario == papel):
    if(opcionMaquina == papel):
        print("empate")
    elif (opcionMaquina == tijera):
        print("perdiste")
    elif (opcionMaquina == piedra):
        print("ganaste")
elif (opcionUsuario == tijera):
    if(opcionMaquina == tijera):
        print("empate")
    elif (opcionMaquina == piedra):
        print("perdiste")
    elif (opcionMaquina == papel):
        print("ganaste")
else:

    print("opcion no valida")





