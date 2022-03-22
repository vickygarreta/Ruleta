import random
from turtle import color
import matplotlib.pyplot as plt

x = []
y= []
hi =[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

def funcion(rep):
    c=0; suma=0; i=0
    for i in range(rep):
        nRandom = random.randint (0,36)
        suma = suma + nRandom
        hi[nRandom] += 1
        c +=1
        x.append(c)
        y.append(suma/c)
    return (suma/rep)

print("Ingrese la cantidad de repeticiones que quiere ejecutar: ", end=""); rep = int(input())

prom = funcion(rep)
print("El promedio es: ", prom)

# Esto hace la linea del promedio
x1 = [0, rep]
y2 = [prom, prom]
plt.plot(x1,y2, color='r')
plt.xlabel("Nro de tiro")
plt.ylabel("Resultado del tiro")
plt.title("Simulacion ruleta")

# Esto hace la grafica de los tiros
plt.plot(x,y, color='b') 

# Esto hace la frecuencia relativa
for i in range(36):
    x.append(i)
    y.append(hi[i])
plt.plot(x,y, color='b') 

print(hi)



plt.show()
