import random as ran
from cmath import sqrt
from xmlrpc.client import Boolean
import numpy as np # importando numpy
from turtle import color
import matplotlib.pyplot as plt
from pyparsing import col 
from scipy import stats # importando scipy.stats

numeroRandomObtenido = 0
apuesta_minima_ruleta = 10000
dinero_ganado_paridad = 15000
rojo = "Rojo"
negro = "Negro"
par = "Par"
impar = "Impar"
docena1 = "1ra docena"
docena2 = "2da docena"
docena3 = "3ra docena"
falta = "1-18"
pasa = "19-36"

columna1 = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
columna2 = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
columna3 = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

numerosRojos = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]

# Definir apuesta por columna y por docena, ademas hacer que se pueda apostar por muchos a la vez
# Modificar la opcion 1 para que sea solo numero, y que se pueden apostar a varias opciones

menu = """###### MENU RULETA #######
1. JUGAR
2. SALIR
Elige: """

explicacion_ruleta = f"""\nSe puede apostar por:
1) Numero y color: si acertás ambos, la apuesta se multiplica por 10. Si no, se pierde la apuesta
2) Solamente color: si se acierta el color, la apuesta se multiplica por 2. Si no, se pierde la apuesta
3) Solo paridad: si se acierta par o impar, se ganan 15000. Si no, se pierde la apuesta.
Los numeros van del 0 al 36, colores son rojo y negro, paridades son par e impar\n"""


def solicitarDineroRuleta(saldoGlobal, apuestaActual):
    dinero_apostado = 0
    if  (saldoGlobal-apuestaActual) >= apuesta_minima_ruleta:
        print(f"Tu saldo actual es: {saldoGlobal-apuestaActual}")
        dinero_apostado = float(input(f"¿Cuanto apostás? Debe ser al menos '{apuesta_minima_ruleta}' pesos, y no debe superar el saldo: "))
        band = True
        while band:
            if(dinero_apostado >= apuesta_minima_ruleta):
                if ((saldoGlobal-(apuestaActual + dinero_apostado)) >= 0):
                    apuestaActual += dinero_apostado
                    band = False
                else:
                    dinero_apostado = float(input(f"Te pasaste de la apuesta maxima que podes hacer, la cual es '{(saldoGlobal-apuestaActual)}' pesos: "))
            else: 
                dinero_apostado = float(input(f"Estas apostando menos de lo sugerida, ingresa una valor >= a 10000: "))
    else:
        print("Tu saldo no llega al minimo para apostar.")
    return dinero_apostado, apuestaActual

def pedirNumero():
    numero = int(input("Elige un numero entre 0 y 36: "))
    band = True
    while (band): 
        if 0 < numero < 36:
            band = False
            return numero
        else:
            band = True

def validaSaldo(saldo):
    band = False
    if saldo < apuesta_minima_ruleta:
        print(f"Necesitas de al menos {apuesta_minima_ruleta} pesos para jugar.")
        band = True
    return band

def main():
    saldo_global = 50000 #El saldo con el que se inicia
    eleccion = ""
    while eleccion != "2":
        eleccion = input(menu)
        if eleccion == "1":
            print(f"Dinero disponible de su cuenta: {saldo_global}")
            if(validaSaldo(saldo_global)):
                continue
            matrizApuestas = []
            apuestaActual = 0
            print(explicacion_ruleta)
            eleccion_ruleta = ""
            while eleccion_ruleta != "8":
                print(f"Dinero disponible para esta ronda: {saldo_global-apuestaActual}")
                eleccion_ruleta = input("""\t1. Número\n\t2. Color\n\t3. Paridad (par e impar)\n\t4. 12's\n\t5. 1-18 y/o 19-36\n\t6. 2 to 1\n\t7. Girar la ruleta\n\t8. Volver\n\tElige: """)
#Opcion 1 (Número)
                if eleccion_ruleta == "1":
                    if(validaSaldo(saldo_global)):
                        break
                    dinero_apostado, apuestaActual = solicitarDineroRuleta(saldo_global, apuestaActual)
                    if (dinero_apostado == 0):
                        break
                    numero_usuario = pedirNumero()
                    matrizApuestas.append([numero_usuario, dinero_apostado])
#Opcion 2 (Color)
                elif eleccion_ruleta == "2":
                    if(validaSaldo(saldo_global)):
                        break
                    dinero_apostado, apuestaActual = solicitarDineroRuleta(saldo_global, apuestaActual)
                    if (dinero_apostado == 0):
                        break
                    color_eleccion_usuario = input("\t1.Rojo\n\t2.Negro\n\tElige: ")         #Para UN SOLO color
                    if color_eleccion_usuario == "1":
                        matrizApuestas.append([rojo, dinero_apostado])
                    elif color_eleccion_usuario == "2":
                        matrizApuestas.append([negro, dinero_apostado])
                    else:
                        print("Ingresó otra opción.")
                        break
#Opcion 3 (paridad)
                elif eleccion_ruleta == "3":
                    if(validaSaldo(saldo_global)):
                        break
                    dinero_apostado,apuestaActual = solicitarDineroRuleta(saldo_global, apuestaActual)
                    if (dinero_apostado == 0):
                        break
                    paridad_eleccion_usuario = input("\t1.Par\n\t2.Impar\n\tElige: ")       #Para UNA SOLA paridad
                    if paridad_eleccion_usuario == "1":
                        matrizApuestas.append([par, dinero_apostado])
                    elif paridad_eleccion_usuario == "2":
                        matrizApuestas.append([impar, dinero_apostado])
                    else:
                        print("Ingresó otra opción.")
                        break
#Opcion 4 12's
                elif eleccion_ruleta == "4":
                    if(validaSaldo(saldo_global)):
                        break
                    dinero_apostado,apuestaActual = solicitarDineroRuleta(saldo_global, apuestaActual)
                    if (dinero_apostado == 0):
                        break
                    docena_eleccion_usuario = input("\t1.1ra docena\n\t2.2da docena\n\t3.3ra docena\n\tElige: ")   #Para UNA SOLA docena
                    if docena_eleccion_usuario == "1":
                        matrizApuestas.append([docena1, dinero_apostado])
                    elif docena_eleccion_usuario == "2":
                        matrizApuestas.append([docena2, dinero_apostado])
                    elif docena_eleccion_usuario == "3":
                        matrizApuestas.append([docena3, dinero_apostado])
                    else:
                        print("Ingresó otra opción.")
                        break
#Opcion 5 1-18 o 19-36
                elif eleccion_ruleta == "5":
                    if(validaSaldo(saldo_global)):
                        break
                    dinero_apostado,apuestaActual = solicitarDineroRuleta(saldo_global, apuestaActual)
                    if (dinero_apostado == 0):
                        break
                    faltapasa_eleccion_usuario = input("\t1.1-18\n\t2.19-36\n\tElige: ")   #Para UNA SOLA 
                    if faltapasa_eleccion_usuario == "1":
                        matrizApuestas.append([falta, dinero_apostado])
                    elif faltapasa_eleccion_usuario == "2":
                        matrizApuestas.append([pasa, dinero_apostado])
                    else:
                        print("Ingresó otra opción.")
                        break
#Opcion 6 columnas
                elif eleccion_ruleta == "6":
                    if(validaSaldo(saldo_global)):
                        break
                    dinero_apostado,apuestaActual = solicitarDineroRuleta(saldo_global, apuestaActual)
                    if (dinero_apostado == 0):
                        break
                    columna_eleccion_usuario = input("\t1.1ra columna\n\t2.2da columna\n\t3.3ra columna\n\tElige: ")   #Para UNA SOLA docena
                    if columna_eleccion_usuario == "1":
                        matrizApuestas.append([columna1, dinero_apostado])
                    elif columna_eleccion_usuario == "2":
                        matrizApuestas.append([columna2, dinero_apostado])
                    elif columna_eleccion_usuario == "3":
                        matrizApuestas.append([columna3, dinero_apostado])
                    else:
                        print("Ingresó otra opción.")
                        break
#Opcion 7 columnas
                elif eleccion_ruleta == "7": #genero el numero y analizo cada condicion
                    nRandom = ran.randint (0,36)
                    saldo_global -= dinero_apostado # le descuento al salgoGlobal lo apostado
                    ganancia = 0
                    for i in range(np.size(matrizApuestas)):
                        m = matrizApuestas[i]

                        # Si acerto el Numero
                        if(m[0] == nRandom): 
                            ganancia += m[1]*32
                        # Si acerto el Color
                        if(nRandom in numerosRojos and m[0] == rojo) or (nRandom not in numerosRojos and m[0] == negro):
                                ganancia += m[1]*32 # Nose si se multiplica por 32
                        # Si acerto la paridad
                        if (nRandom %2 == 0 and m[0] == par) or (nRandom % 2 != 0 and m[0] == impar):
                            ganancia += m[1] * 2 # Nose si se multiplica por 2
                        # Si acerto los 12's
                        if (nRandom >= 1 and nRandom <= 12 and m[1] == docena1) or (nRandom >= 13 and nRandom <= 24 and m[1] == docena2) or (nRandom >= 25 and nRandom <= 36 and m[1] == docena3):
                            ganancia += m[1] * 2 # Nose si se multiplica por 2
                        # Si acerto los 1-18 o 19-36
                        if (nRandom >= 1 and nRandom <= 18 and m[1] == falta) or (nRandom >= 19 and nRandom <= 36 and m[1] == pasa):
                            ganancia += m[1] * 2 # Nose si se multiplica por 2
                        if (nRandom in columna1 and m[1] == columna1) or (nRandom in columna2 and m[1] == columna2) or (nRandom in columna3 and m[1] == columna3):
                            ganancia += m[1] * 2 # Nose si se multiplica por 2

                    saldo_global += ganancia # Sumo la ganancia q haya tenido el usuario

            print(f"Saldo final: {saldo_global}") 
main()
