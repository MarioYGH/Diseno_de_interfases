#from random import random # una funcion
import random as rnd #Toda la libreria 

r1 = rnd.random()
print(r1)

r2 = rnd.randrange(10,36) #random con rango del 10 al 35, va de a to b-1
print(r2)

r3 = rnd.randint(10,35) #aca si es del 1 al 35
print(r3)

def suma(a,b):
    r = a + b
    return r

def aleatorio():
    r = rnd.random()
    return r

r5 = aleatorio()
print(r5)


